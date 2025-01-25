from gendiff.consts import NEW_VALUE, OLD_VALUE, STATUS, VALUE


def build_diff(dict1, dict2):
    uniq_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff_dict = {}
    for key in uniq_keys:
        if key not in dict1:
            diff_dict[key] = {STATUS: "added", VALUE: dict2[key]}
        elif key not in dict2:
            diff_dict[key] = {STATUS: "deleted", VALUE: dict1[key]}
        elif dict1[key] == dict2[key]:
            diff_dict[key] = {STATUS: "unchanged", VALUE: dict1[key]}
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff_dict[key] = {
                STATUS: "nested", VALUE: build_diff(dict1[key], dict2[key])
            }
        else:
            diff_dict[key] = {
                STATUS: "changed", OLD_VALUE: dict1[key], NEW_VALUE: dict2[key]
            }
    return diff_dict
