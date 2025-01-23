from gendiff.formater.stylish import stylish
from gendiff.builder import build_diff
from gendiff.loader import load_supp_file_form


def generate_diff(path_file1, path_file2):
    dict1, dict2 = (
        load_supp_file_form(path_file1),
        load_supp_file_form(path_file2)
    )
    diff = build_diff(dict1, dict2)
    return stylish(diff)
