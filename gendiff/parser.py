import json

import yaml


def load_supp_form_file(path):
    path_str = str(path)
    try:
        with open(path_str) as f:
            if path_str.endswith(".json"):
                return json.load(f)
            elif path_str.endswith((".yml", "yaml")):
                return yaml.safe_load(f)
            elif path_str.endswith(".txt"):
                return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path_str}")
