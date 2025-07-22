import requests
from requests.auth import HTTPBasicAuth
import json
from openai import OpenAI
from config import Config
import numpy as np

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
question_completeness_checker = [
    {
        "name": "question_completeness_checking_function",
        "description": "Question Completeness Checker.",
        "parameters": {
            "type": "object",
            "properties": {
                "completeness": {
                    "type": "string",
                    "description": "Question completeness validation response",
                }
            }
        }

    }
]
question_generation_function = [
    {
        "name": "question_generation_function",
        "description": "Processes a list of query outputs including unique question id, original query, formal question, and entities.",
        "parameters": {
            "type": "object",
            "properties": {
                "outputs": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "A unique identifier for the query."
                            },
                            "original_query": {
                                "type": "string",
                                "description": "The user's natural language query."
                            },
                            "formal_question": {
                                "type": "string",
                                "description": "A formalized version of the user's question."
                            },
                            "entities": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "mention": {
                                            "type": "string",
                                            "description": "Entity as mentioned in the question."
                                        },
                                        "uri": {
                                            "type": "string",
                                            "description": "The knowledge base URI for the entity."
                                        }
                                    },
                                    "required": ["mention", "uri"]
                                }
                            }
                        },
                        "required": ["id", "original_query", "formal_question", "entities"]
                    }
                }
            },
            "required": ["outputs"]
        }
    }
]


def compute_confidence_score(logprobs):
    all_logprobs = []
    for token_info in logprobs:
        logprob = token_info.logprob  # this is a float
        all_logprobs.append(logprob)
    token_probs = [np.exp(lp) for lp in all_logprobs]
    confidence_score = np.prod(token_probs) ** (1 / len(token_probs))

    return confidence_score


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
        # print(f"Response: {response_data}")
        if 'generated_text' in response_data:
            return response_data['generated_text']
        else:
            return response_data
    else:
        print(f"Error: {response.status_code}")
        print("Response text:", response.text)
        return None


def chatai_models(prompt, model, function_call_flag = 1):
    function_call = sparql_generation_function
    flag = False
    if function_call_flag == 2:
        function_call = question_completeness_checker
        flag = True
    elif function_call_flag == 3:
        function_call = question_generation_function
    api_key = Config.LLMS['chatai']['chatai_api_key']
    base_url = Config.LLMS['chatai']['url']
    model = model # Config.LLMS['chatai']['model']
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    # messages = [{"role": "user", "content": prompt}]
    messages = [ {"role": "system", "content": "You are an experienced knowledge graph expert."},
        {"role": "user", "content": prompt}
    ]
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
        functions=function_call,
        function_call='auto',
        temperature=0,
        logprobs=True
    )
    try:
        result = json.loads(chat_completion.choices[0].message.content)
        # print(result)
        if flag:
            return result
        logprobs = chat_completion.choices[0].logprobs.content
        confidence_score = compute_confidence_score(logprobs)
        # print("Confidence score:", confidence_score)
        return result, confidence_score
    except Exception as e:
        print(f"An error occurred while generating response: {e}")
        return None


def chatgpt(prompt, function_call_flag = 1):

    function_call = sparql_generation_function
    if function_call_flag == 2:
        function_call = question_completeness_checker
    elif function_call_flag == 3:
        function_call = question_generation_function

    model = Config.LLMS['openai']['model']
    api_key = Config.LLMS['openai']['open_api_key']
    client = OpenAI(
        api_key=api_key
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        functions=function_call,
        function_call='auto'
    )
    try:
        json_response = json.loads(completion.choices[0].message.function_call.arguments)
        # print(json_response)
        return json_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


if __name__ == '__main__':
    chatai_models("")

