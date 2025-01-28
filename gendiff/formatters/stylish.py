from itertools import chain

from gendiff.consts import NEW_VALUE, OLD_VALUE, VALUE


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)


def stylish(diff, depth=0, replacer=" ", repl_count=4):
    if not isinstance(diff, dict):
        return format_value(diff)
    current_deep = replacer * depth
    deep_indent = repl_count + depth
    new_deep_indent = replacer * deep_indent
    form_indent = {
        "add": replacer * (deep_indent - 2) + "+ ",
        "remove": replacer * (deep_indent - 2) + "- ",
        "empty": replacer * (deep_indent - 2) + "  "
    }
    result = []
    for key, val in diff.items():
        if isinstance(val, dict) and "added" in val.values():
            result.append(f"{form_indent["add"]}{key}: "
                          f"{stylish(val[VALUE], deep_indent)}")
        elif isinstance(val, dict) and "removed" in val.values():
            result.append(f"{form_indent["remove"]}{key}: "
                          f"{stylish(val[VALUE], deep_indent)}")
        elif isinstance(val, dict) and "unchanged" in val.values():
            result.append(f"{form_indent["empty"]}{key}: "
                          f"{stylish(val[VALUE], deep_indent)}")
        elif isinstance(val, dict) and "changed" in val.values():
            result.append(f"{form_indent["remove"]}{key}: "
                          f"{stylish(val[OLD_VALUE], deep_indent)}")
            result.append(f"{form_indent["add"]}{key}: "
                          f"{stylish(val[NEW_VALUE], deep_indent)}")
        elif isinstance(val, dict) and "nested" in val.values():
            result.append(f"{new_deep_indent}{key}: "
                          f"{stylish(val[VALUE], deep_indent)}")
        else:
            result.append(f"{new_deep_indent}{key}: "
                          f"{stylish(val, deep_indent)}")
    return "\n".join(chain("{", result, [current_deep + "}"]))
