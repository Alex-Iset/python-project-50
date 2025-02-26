import json

import yaml


def file_loader(path, extension):
    with open(path) as f:
        match extension:
            case '.json':
                return json.load(f)
            case '.yml' | '.yaml':
                return yaml.safe_load(f)
