import json

import yaml


def load_supp_form_file(path):
    try:
        with open(path) as f:
            if path.endswith(".json"):
                return json.load(f)
            elif path.endswith((".yml", "yaml")):
                return yaml.safe_load(f)
            elif path.endswith(".txt"):
                return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
