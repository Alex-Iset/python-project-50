import json

import yaml


def load_json_file(path):
    with open(path) as f:
        return json.load(f)


def load_yaml_file(path):
    with open(path) as f:
        return yaml.safe_load(f)
