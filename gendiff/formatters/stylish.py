from gendiff.consts import INDENT, NEW_VALUE, OLD_VALUE, STATUS, STATUSES, VALUE


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def build_indent(depth):
    return INDENT[:-2] + INDENT * depth


def format_data(data, depth):
    string_data = '\n'.join(data)
    last_indent = build_indent(depth)[:-2]
    return f'{string_data}\n{last_indent}'


def put_into_braces(formatted_data):
    return f'{{\n{formatted_data}}}'


def stylish(diff):
    def _iter_stylish(data, depth=0):
        if not isinstance(data, dict):
            return format_value(data)

        result = []
        for key, val in data.items():
            indent = build_indent(depth)
            if isinstance(val, dict):
                status = val.get(STATUS)
                value = val.get(VALUE)
                formatted_value = _iter_stylish(value, depth + 1)
                match status:
                    case STATUSES.ADDED:
                        result.append(f'{indent}+ {key}: {formatted_value}')
                    case STATUSES.REMOVED:
                        result.append(f'{indent}- {key}: {formatted_value}')
                    case STATUSES.UNCHANGED:
                        result.append(f'{indent}  {key}: {formatted_value}')
                    case STATUSES.UPDATED:
                        old_value = _iter_stylish(val.get(OLD_VALUE), depth + 1)
                        new_value = _iter_stylish(val.get(NEW_VALUE), depth + 1)
                        result.append(f'{indent}- {key}: {old_value}')
                        result.append(f'{indent}+ {key}: {new_value}')
                    case STATUSES.NESTED:
                        result.append(f'{indent}  {key}: {formatted_value}')
                    case _:
                        formatted_value = _iter_stylish(val, depth + 1)
                        result.append(f'{indent}  {key}: {formatted_value}')
            else:
                formatted_value = _iter_stylish(val, depth + 1)
                result.append(f'{indent}  {key}: {formatted_value}')
        return put_into_braces(format_data(result, depth))
    return _iter_stylish(diff)
