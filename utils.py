import json
import requests
from config import Config

def extruct_values(results):
    return_result = []
    for result in results["results"]["bindings"]:
        converted_result = {}
        for key, value_info in result.items():
            value = value_info.get('value')
            if value:
                converted_result[key] = value
        return_result.append(converted_result)
    return return_result


def get_examples(key, file_path="examples.json"):
    with open(file_path, 'r', encoding='utf-8') as file:
        examples_data = json.load(file)
    examples = '\n'.join(f"{key}: {value}" for d in examples_data.get(key, None) for key, value in d.items())
    return examples


def dblp_entity_linker(question):
    entity_linker_url = Config.DBLP_ENTITY_LINKER
    headers = {"Content-Type": "application/json"}
    data = {"question": question}
    try:
        response = requests.post(entity_linker_url, json=data, headers=headers, timeout=100)
        response.raise_for_status()
        if response:
            result = response.json()
            entities = {label: uri for entry in result['entitylinkingresults'][0]['result'] for uri, label in [entry[1]]}
            return entities
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    result = dblp_entity_linker("where does Ricardo Usbeck work?")
    print(result)