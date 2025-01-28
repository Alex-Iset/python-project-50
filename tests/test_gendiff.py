import os

from gendiff import generate_diff
from gendiff.loader import load_supp_form_file


def get_test_data_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


file1 = get_test_data_path('file1.json')  # нужно будет переделать
file2 = get_test_data_path('file2.json')
file3 = get_test_data_path('file1.yaml')
file4 = get_test_data_path('file2.yaml')

def test_gendiff(): # нужно будет переделать
    stylish = load_supp_form_file(
        get_test_data_path('stylish_output.txt')
    )
    plain = load_supp_form_file(
        get_test_data_path('plain_output.txt')
    )
    json_format = load_supp_form_file(
        get_test_data_path('json_format_output.txt')
    )
    assert generate_diff(file1, file2, "stylish") == stylish
    assert generate_diff(file3, file4, "stylish") == stylish
    assert generate_diff(file1, file2, "plain") == plain
    assert generate_diff(file3, file4, "plain") == plain
    assert generate_diff(file1, file2, "json") == json_format
    assert generate_diff(file3, file4, "json") == json_format
