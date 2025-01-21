import json
import os

import yaml

from gendiff import diff, load_json, load_yaml


def get_test_data_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


file1 = load_json(get_test_data_path('file1.json'))
file2 = load_json(get_test_data_path('file2.json'))
file3 = load_yaml(get_test_data_path('file1.yaml'))
file4 = load_yaml(get_test_data_path('file2.yaml'))
result = '''{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}'''


def test_json_gendiff():
    assert diff(file1, file2) == result


def test_yaml_gendiff():
    assert diff(file1, file2) == result
