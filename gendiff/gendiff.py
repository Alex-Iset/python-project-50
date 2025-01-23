from gendiff.formater.stylish import stylish
from gendiff.loader import load_supp_file_form


def added(value):
    return {
        "added": value
    }


def deleted(value):
    return {
        "deleted": value
    }


def changed(old_value, new_value):
    return {
        "old_changed": old_value,
        "new_changed": new_value
    }


def unchanged(value):
    return {
        "unchanged": value
    }


def nested(value):
    return {
        "nested": value
    }


def build_diff(dict1, dict2):
    uniq_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff_dict = {}
    for key in uniq_keys:
        if key not in dict1:
            diff_dict[key] = added(dict2[key])
        elif key not in dict2:
            diff_dict[key] = deleted(dict1[key])
        elif dict1[key] == dict2[key]:
            diff_dict[key] = unchanged(dict1[key])
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff_dict[key] = nested(build_diff(dict1[key], dict2[key]))
        else:
            diff_dict[key] = changed(dict1[key], dict2[key])
    return diff_dict


def generate_diff(path_file1, path_file2):
    dict1, dict2 = (
        load_supp_file_form(path_file1),
        load_supp_file_form(path_file2)
    )
    diff = build_diff(dict1, dict2)
    return diff
