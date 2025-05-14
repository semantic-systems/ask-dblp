import requests
from requests.auth import HTTPBasicAuth
import json
from prompts import question_to_sparql_prompt
import dblp_schema
from openai import OpenAI
import re
from config import Config
import numpy as np

def extract_triple_quoted_string(text):
    match = re.search(r'"""\s*(.*?)\s*"""', text, re.DOTALL)
    return match.group(1) if match else None


def compute_confidence_score(logprobs):
    all_logprobs = []
    for token_info in logprobs:
        logprob = token_info.logprob  # this is a float
        all_logprobs.append(logprob)
    token_probs = [np.exp(lp) for lp in all_logprobs]
    confidence_score = np.prod(token_probs) ** (1 / len(token_probs))

    return confidence_score

def get_question_to_sparql_prompt(question):
    prompt_template = question_to_sparql_prompt.QUESTION_TO_SPARQL_PROMPT
    prompt = prompt_template.format(
        question=question,
        dblp_schema=dblp_schema.properties_uri_and_description,
    )
    return prompt


def question_to_sparql(question, llm='chatai'):
    prompt = get_question_to_sparql_prompt(question)
    # if llm == 'chatgpt':
    #     sparql = chatgpt(prompt)
    #     return sparql['sparql']
    # sparql_result = llama(prompt)
    sparql_result, confidence = chatai_models(prompt)
    print(sparql_result)
    return sparql_result['sparql'], confidence


def llama(user_prompt, sys_prompt_string="You are an experienced knowledge graph expert."):
    server_url = Config.LLMS['llama3']['url']
    messages = [
        {"role": "system", "content": sys_prompt_string},
        {"role": "user", "content": user_prompt}]
    payload = {
        "messages": messages,
        "temperature": 0.001
    }
    response = requests.post(
        server_url,
        headers={'Content-Type': 'application/json'},
        auth=HTTPBasicAuth(Config.LLMS['llama3']['username'], Config.LLMS['llama3']['password']),
        json=payload
    )
    if response.status_code == 200:
        response_data = response.json()
        # print(f"Model: {response_data["model"]}")
        print(f"Response: {response_data}")
        if 'generated_text' in response_data:
            return response_data['generated_text']
        else:
            return response_data
    else:
        print(f"Error: {response.status_code}")
        print("Response text:", response.text)
        return None


def chatai_models(prompt):
    sparql_generation_function = [
        {
            "name": "sparql_generation_function",
            "description": "Generate a SPARQL query for the given question.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sparql": {
                        "type": "string",
                        "description": "SPARQL of a given question",
                    }
                }
            }

        }
    ]
    api_key = Config.LLMS['chatai']['chatai_api_key']
    base_url = Config.LLMS['chatai']['url']
    model = Config.LLMS['chatai']['model']
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    messages = [{"role": "user", "content": prompt}]
    # messages = [ {"role": "system", "content": "You are an experienced knowledge graph expert."},
    #     {"role": "user", "content": messages}
    # ]
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
        functions=sparql_generation_function,
        function_call='auto',
        temperature=0,
        logprobs=True
    )
    try:
        result = json.loads(chat_completion.choices[0].message.content)
        logprobs = chat_completion.choices[0].logprobs.content
        confidence_score = compute_confidence_score(logprobs)
        print("Confidence score:", confidence_score)
        return result, confidence_score
    except Exception as e:
        print(f"An error occurred while generating answer: {e}")
        return None


def chatgpt(prompt):
    sparql_generation_function = [
        {
            "name": "sparql_generation_function",
            "description": "Generate a SPARQL query for the given question.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sparql": {
                        "type": "string",
                        "description": "SPARQL of a given question",
                    }
                }
            }

        }
    ]

    model = Config.LLMS['openai']['model']
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        functions=sparql_generation_function,
        function_call='auto'
    )
    try:
        json_response = json.loads(completion.choices[0].message.function_call.arguments)
        print(json_response)
        return json_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


if __name__ == '__main__':
    chatai_models("")

