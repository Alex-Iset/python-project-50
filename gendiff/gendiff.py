from gendiff.builder import build_diff
from gendiff.formater.stylish import stylish
from gendiff.loader import load_supp_form_file


def generate_diff(path_file1, path_file2):
    dict1 = load_supp_form_file(path_file1)
    dict2 = load_supp_form_file(path_file2)
    diff = build_diff(dict1, dict2)
    return stylish(diff)
