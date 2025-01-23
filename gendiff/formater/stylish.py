from itertools import chain


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)


def stylish(data, replacer=' ', repl_count=4):
    def inner(value, depth):
        if not isinstance(value, dict):
            return format_value(value)
        repl_depth = replacer * depth
        new_depth = repl_count + depth
        new_repl_depth = replacer * new_depth
        result = []
        for key, val in value.items():
            result.append(f'{new_repl_depth}{key}: {inner(val, new_depth)}')
        return '\n'.join(chain('{', result, [repl_depth + '}']))
    return inner(data, 0)
