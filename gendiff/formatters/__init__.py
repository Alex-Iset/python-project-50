from gendiff.consts import FORMATS
from gendiff.formatters.json import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def get_formatter(diff, formatter):
    match formatter:
        case FORMATS.STYLISH:
            return stylish(diff)
        case FORMATS.PLAIN:
            return plain(diff)
        case FORMATS.JSON:
            return json_format(diff)
