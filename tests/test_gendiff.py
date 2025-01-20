import json
import os

from gendiff import diff


def get_test_data_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read(file_path):
    with open(file_path) as f:
        return json.load(f)


file1 = read(get_test_data_path('file1.json'))
file2 = read(get_test_data_path('file2.json'))
result = '''{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}'''


def test_gendiff():
    assert diff(file1, file2) == result
