from itertools import chain

from gendiff.consts import NEW_VALUE, OLD_VALUE, VALUE


def form_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)


def form_repl(depth, flag=""):
    forms = {
        "add": " " * (depth - 2) + '+ ',
        "remove": " " * (depth - 2) + '- ',
        "empty": " " * (depth - 2) + '  '
    }
    return forms[flag]


def stylish(data, depth=0, replacer=" ", repl_count=4):
    if not isinstance(data, dict):
        return form_value(data)
    current_repl = replacer * depth
    deep_repl = repl_count + depth
    new_deep_repl = replacer * deep_repl
    result = []
    for key, val in data.items():
        if isinstance(val, dict) and "added" in val.values():
            result.append(f"{form_repl(deep_repl, "add")}{key}: "
                          f"{stylish(val[VALUE], deep_repl)}")
        elif isinstance(val, dict) and "removed" in val.values():
            result.append(f"{form_repl(deep_repl, "remove")}{key}: "
                          f"{stylish(val[VALUE], deep_repl)}")
        elif isinstance(val, dict) and "unchanged" in val.values():
            result.append(f"{form_repl(deep_repl, "empty")}{key}: "
                          f"{stylish(val[VALUE], deep_repl)}")
        elif isinstance(val, dict) and "changed" in val.values():
            result.append(f"{form_repl(deep_repl, "remove")}{key}: "
                          f"{stylish(val[OLD_VALUE], deep_repl)}")
            result.append(f"{form_repl(deep_repl, "add")}{key}: "
                          f"{stylish(val[NEW_VALUE], deep_repl)}")
        elif isinstance(val, dict) and "nested" in val.values():
            result.append(f"{new_deep_repl}{key}: "
                          f"{stylish(val[VALUE], deep_repl)}")
        else:
            result.append(f"{new_deep_repl}{key}: "
                          f"{stylish(val, deep_repl)}")
    return "\n".join(chain("{", result, [current_repl + "}"]))
