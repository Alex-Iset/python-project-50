import json
import os

import yaml


def file_loader(path):
    extension = os.path.splitext(path)[1]
    with open(path) as f:
        match extension:
            case ".json":
                return json.load(f)
            case ".yml" | ".yaml":
                return yaml.safe_load(f)
            case ".txt":
                return f.read()
