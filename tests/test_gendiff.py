import os

from gendiff import diff


def get_test_data_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read_result_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")


file1 = get_test_data_path('file1.json')  # нужно будет переделать
file2 = get_test_data_path('file2.json')  # нужно будет переделать
file3 = get_test_data_path('file1.yaml')  # нужно будет переделать
file4 = get_test_data_path('file2.yaml')  # нужно будет переделать


def test_gendiff():
    result = read_result_file(
        get_test_data_path('result_json_yaml.txt')
    )
    assert diff(file1, file2) == result
    assert diff(file3, file4) == result
