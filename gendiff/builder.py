from gendiff.consts import NEW_VALUE, OLD_VALUE, STATUS, VALUE


def added(value):
    return {STATUS: "added", VALUE: value}


def removed(value):
    return {STATUS: "removed", VALUE: value}


def unchanged(value):
    return {STATUS: "unchanged", VALUE: value}


def changed(old_value, new_value):
    return {
        STATUS: "changed",
        OLD_VALUE: old_value,
        NEW_VALUE: new_value
    }


def nested(value):
    return {STATUS: "nested", VALUE: value}


def build_diff(dict1, dict2):
    uniq_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff_dict = {}
    for key in uniq_keys:
        if key not in dict1:
            diff_dict[key] = added(dict2[key])
        elif key not in dict2:
            diff_dict[key] = removed(dict1[key])
        elif dict1[key] == dict2[key]:
            diff_dict[key] = unchanged(dict1[key])
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff_dict[key] = nested(build_diff(dict1[key], dict2[key]))
        else:
            diff_dict[key] = changed(dict1[key], dict2[key])
    return diff_dict
