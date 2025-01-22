import json

import yaml


def load_json_file(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")


def load_yaml_file(path):
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")


def load_supp_file_form(path):
    if path.endswith('.json'):
        return load_json_file(path)
    elif path.endswith(('.yml', 'yaml')):
        return load_yaml_file(path)
    else:
        raise ValueError(f'Unsupported file format: {path}')
