import json

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