from itertools import chain

from gendiff.consts import NEW_VALUE, OLD_VALUE, VALUE


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)


def stylish(diff, replacer=" ", repl_count=4):
    def inner(value, depth):
        if not isinstance(value, dict):
            return format_value(value)
        current_deep = replacer * depth
        deep_indent = repl_count + depth
        new_deep_indent = replacer * deep_indent
        result = []
        for key, val in value.items():
            form_repl = {
                "add": replacer * (deep_indent - 2) + '+ ',
                "remove": replacer * (deep_indent - 2) + '- ',
                "empty": replacer * (deep_indent - 2) + '  '
            }
            if isinstance(val, dict) and "added" in val.values():
                result.append(f"{form_repl["add"]}{key}: "
                              f"{inner(val[VALUE], deep_indent)}")
            elif isinstance(val, dict) and "removed" in val.values():
                result.append(f"{form_repl["remove"]}{key}: "
                              f"{inner(val[VALUE], deep_indent)}")
            elif isinstance(val, dict) and "unchanged" in val.values():
                result.append(f"{form_repl["empty"]}{key}: "
                              f"{inner(val[VALUE], deep_indent)}")
            elif isinstance(val, dict) and "changed" in val.values():
                result.append(f"{form_repl["remove"]}{key}: "
                              f"{inner(val[OLD_VALUE], deep_indent)}")
                result.append(f"{form_repl["add"]}{key}: "
                              f"{inner(val[NEW_VALUE], deep_indent)}")
            elif isinstance(val, dict) and "nested" in val.values():
                result.append(f"{new_deep_indent}{key}: "
                              f"{inner(val[VALUE], deep_indent)}")
            else:
                result.append(f"{new_deep_indent}{key}: "
                              f"{inner(val, deep_indent)}")
        return "\n".join(chain("{", result, [current_deep + "}"]))
    return inner(diff, 0)
