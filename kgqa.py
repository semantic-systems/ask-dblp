import json
import logging

import llms
import requests
from config import Config
from prompts import question_to_sparql_prompt, question_checker_prompt
import dblp_schema
import utils
import re

def parse_completness_check_result(raw_content):
    result = {"completeness": None, "feedback": None}
    try:
        parsed = json.loads(raw_content)
        if isinstance(parsed, dict):
            result["completeness"] = parsed.get("completeness")
            result["feedback"] = parsed.get("feedback")
            return result
    except json.JSONDecodeError:
        pass

    # Step 2: Regex fallback for malformed or escaped JSON-like strings
    completeness_match = re.search(r'"completeness"\s*:\s*"([^"]+)"', raw_content)
    feedback_match = re.search(r'"feedback"\s*:\s*"([^"]+)"', raw_content)

    if completeness_match:
        result["completeness"] = completeness_match.group(1).encode().decode("unicode_escape").strip()

    if feedback_match:
        result["feedback"] = feedback_match.group(1).encode().decode("unicode_escape").strip()

    return result


def extract_sparql(response_content):
    """
    Extracts a SPARQL query string from LLM output.
    Attempts JSON parsing first, then falls back to regex-based extraction.
    Args:
        response_content (str): Raw LLM output string.
    Returns:
        str | None: The SPARQL query if found, else None.
    """
    try:
        data = json.loads(response_content)
        sparql = data.get("sparql")
        if isinstance(sparql, str) and sparql.strip():
            return sparql.strip()
    except json.JSONDecodeError:
        pass

    # Regex fallback (extract string value of "sparql": "...")
    match = re.search(r'"sparql"\s*:\s*"((?:[^"\\]|\\.)*)"', response_content)
    if match:
        sparql_raw = match.group(1)
        return bytes(sparql_raw, "utf-8").decode("unicode_escape").strip()

    return ""


def clean_label(label, entity_type):
    if "Publication" in entity_type:
        # Remove everything before and including "et al.: "
        label = re.sub(r'^.*?et al\.\:\s*', '', label)
        # Remove trailing year in parentheses like " (2017)"
        label = re.sub(r'\s*\(\d{4}\)$', '', label)
    return label.strip()


def extract_entities_by_group(result):
    """
    Processes entity linking results to extract:
    - All entities per group (with types)
    - The first entity from each group (with type)

    Returns: (output, selected_entities)
    """
    all_entities = []
    selected_entities = []
    for entity in result['entitylinkingresults']:
        if not entity['result']:
            continue
        entity_type = "".join(entity.get('type', [])) or "Unknown"
        entries = []
        for entry in entity['result']:
            original_label = entry[1][1]
            uri = entry[1][0]
            normalized_label = clean_label(original_label, entity_type)
            entries.append({
                "original_label": original_label,
                "normalized_label": normalized_label,
                "uri": uri
            })

        all_entities.append({
            "entity_type": entity_type,
            "entities": entries
        })

        # Use the first item for default used_entities
        first_entry = entries[0]
        selected_entities.append({
            "entity_type": entity_type,
            "normalized_label": first_entry["normalized_label"],
            "original_label": first_entry["original_label"],
            "uri": first_entry["uri"],
        })

    return all_entities, selected_entities


def entity_linker(question):
    entity_linker_url = Config.DBLP_ENTITY_LINKER
    headers = {"Content-Type": "application/json"}
    data = {"question": question}
    try:
        response = requests.post(entity_linker_url, json=data, headers=headers, timeout=1000)
        response.raise_for_status()
        if response:
            all_entities, selected_entities = extract_entities_by_group(response.json())
            return all_entities, selected_entities
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []


def extract_triple_quoted_string(text):
    match = re.search(r'"""\s*(.*?)\s*"""', text, re.DOTALL)
    return match.group(1) if match else None


def get_question_to_sparql_prompt(question, selected_entities=[]):
    examples = utils.get_examples("build_sparql")
    selected_entities_string = ''
    if selected_entities:
        selected_entities_string = '\n  '.join(
            f"ENTITY_LABEL: {entity['normalized_label']} ; ENTITY_TYPE: {entity['entity_type']} ; URI: {entity['uri']}"
            for entity in selected_entities
        )
        # print(selected_entities_string)
        examples = utils.get_examples("buidl_sparql_with_uri")
    prompt_template = question_to_sparql_prompt.QUESTION_TO_SPARQL_PROMPT
    prompt = prompt_template.format(
        question=question,
        dblp_schema=dblp_schema.properties_uri_and_description,
        examples=examples,
        entities=selected_entities_string,
    )
    # print(prompt)
    return prompt


def question_to_sparql(question, llm='chatai'):

    try:
        all_entities, selected_entities = entity_linker(question)
        if not all_entities and selected_entities:
            # print(f"{all_entities} \n {selected_entities}")
            all_entities = []
            selected_entities = []
        prompt = get_question_to_sparql_prompt(question, selected_entities)
        chatai_llm_model = 'qwen2.5-coder-32b-instruct'
        sparql_result, confidence = llms.chatai_models(prompt=prompt, model=chatai_llm_model)
        sparql = extract_sparql(sparql_result)
        return sparql, confidence, all_entities, selected_entities
    except Exception as e:
        logging.error(f"An error occurred during SPARQL Generation: {e}", exc_info=e)
        return "", 0.0, [], []


def question_checker(question):
    question_checker_prompt_template = question_checker_prompt.QUESTION_VALIDATION_PROMPT
    qc_prompt = question_checker_prompt_template.format(question=question)
    chatai_llm_model = 'qwen2.5-coder-32b-instruct'
    validation_result, confidence_score = llms.chatai_models(prompt=qc_prompt, model=chatai_llm_model, function_call_flag=2)
    parse_validation_result = parse_completness_check_result(validation_result)
    return parse_validation_result


if __name__ == '__main__':
    question = "Who were the co-authors of Ashish Vaswani in the paper ‘Attention is all you need’?"
    # result = question_checker(question)
    # print(result)
    # el = entity_linker(question)
    # print(el)
    sparql = question_to_sparql(question)
    print(sparql)
