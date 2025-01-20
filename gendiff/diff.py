import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        dict1 = json.load(f1)
        dict2 = json.load(f2)
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
