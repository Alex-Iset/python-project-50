def build_diff(dict1, dict2):
    uniq_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff_dict = {}
    for key in uniq_keys:
        if key not in dict1:
            diff_dict[f'+ {key}'] = dict2[key]
        elif key not in dict2:
            diff_dict[f'- {key}'] = dict1[key]
        elif dict1[key] == dict2[key]:
            diff_dict[f'  {key}'] = dict1[key]
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff_dict[f'  {key}'] = build_diff(dict1[key], dict2[key])
        else:
            diff_dict[f'- {key}'] = dict1[key]
            diff_dict[f'+ {key}'] = dict2[key]
    return diff_dict
