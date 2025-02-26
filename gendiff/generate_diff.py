import os

from gendiff.build_diff import build_diff
from gendiff.formatters import get_formatter
from gendiff.parser import file_loader


def get_extension(path):
    extension = os.path.splitext(path)[1]
    return extension


def generate_diff(path_file1, path_file2, formatter='stylish'):
    dict1 = file_loader(path_file1, get_extension(path_file1))
    dict2 = file_loader(path_file2, get_extension(path_file2))
    diff = build_diff(dict1, dict2)
    format_diff = get_formatter(diff, formatter)
    return format_diff
