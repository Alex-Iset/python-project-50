from itertools import chain

from gendiff.consts import NEW_VALUE, OLD_VALUE, VALUE


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)


def format_dict(data):
    result = {}
    for key, value in data.items():
        if "value" in value:
            result[key] = value["value"]
        else:
            result[key] = value
    return result


def stylish(data, replacer=" ", repl_count=4):
    def inner(value, depth):
        if not isinstance(value, dict):
            return format_value(value)
        repl_depth = replacer * depth
        new_depth = repl_count + depth
        new_repl_depth = replacer * new_depth
        result = []
        for key, val in value.items():
            form_repl = {
                "add": replacer * (new_depth - 2) + '+ ',
                "del": replacer * (new_depth - 2) + '- ',
                "empty": replacer * (new_depth - 2) + '  '
            }
            if isinstance(val, dict) and "added" in val.values():
                result.append(f"{form_repl["add"]}{key}: "
                              f"{inner(val[VALUE], new_depth)}")
            elif isinstance(val, dict) and "deleted" in val.values():
                result.append(f"{form_repl["del"]}{key}: "
                              f"{inner(val[VALUE], new_depth)}")
            elif isinstance(val, dict) and "unchanged" in val.values():
                result.append(f"{form_repl["empty"]}{key}: "
                              f"{inner(val[VALUE], new_depth)}")
            elif isinstance(val, dict) and "changed" in val.values():
                result.append(f"{form_repl["del"]}{key}: "
                              f"{inner(val[OLD_VALUE], new_depth)}")
                result.append(f"{form_repl["add"]}{key}: "
                              f"{inner(val[NEW_VALUE], new_depth)}")
            elif isinstance(val, dict) and "nested" in val.values():
                result.append(f"{new_repl_depth}{key}: "
                              f"{inner(val[VALUE], new_depth)}")
            else:
                result.append(f"{new_repl_depth}{key}: "
                              f"{inner(val, new_depth)}")
        return "\n".join(chain("{", result, [repl_depth + "}"]))
    return inner(data, 0)
