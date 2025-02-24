from gendiff.formatters.json_format import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def get_formatter(diff, formatter):
    match formatter:
        case "stylish":
            return stylish(diff)
        case "plain":
            return plain(diff)
        case "json":
            return json_format(diff)
