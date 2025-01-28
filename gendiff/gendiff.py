from gendiff.builder import build_diff
from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.loader import load_supp_form_file


def generate_diff(path_file1, path_file2, formatter="stylish"):
    dict1 = load_supp_form_file(path_file1)
    dict2 = load_supp_form_file(path_file2)
    diff = build_diff(dict1, dict2)
    match formatter:
        case "stylish":
            return stylish(diff)
        case "plain":
            return plain(diff)
        case "json":
            return json_format(diff)
