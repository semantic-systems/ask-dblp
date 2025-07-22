import json

def load_json_data(file_name):
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

def write_to_json(result, out_file_path):
    with open(out_file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)
    print("Successfully written to file!")


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