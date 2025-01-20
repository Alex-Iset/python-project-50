import json


def load_json_file(path):
    with open(path) as f:
        return json.load(f)


def generate_diff(file_path1, file_path2):
    dict1, dict2 = load_json_file(file_path1), load_json_file(file_path2)
    result = []
    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result.append(f'  {key}: {dict1[key]}')
            else:
                result.append(f'- {key}: {dict1[key]}')
                result.append(f'+ {key}: {dict2[key]}')
        elif key in dict1:
            result.append(f'- {key}: {dict1[key]}')
        else:
            result.append(f'+ {key}: {dict2[key]}')
    return '{\n' + "\n".join(result) + '\n}'
