from gendiff.consts import NEW_VALUE, OLD_VALUE, STATUS, STATUSES, VALUE


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff):
    def _iter_plain(data, path=''):
        result = []
        for key, val in data.items():
            current_path = f'{path}.{key}' if path else key
            if isinstance(val, dict):
                status = val.get(STATUS)
                match status:
                    case STATUSES.ADDED:
                        result.append(
                            f"Property '{current_path}' "
                            f"was added with value: {format_value(val[VALUE])}"
                        )
                    case STATUSES.REMOVED:
                        result.append(f"Property '{current_path}' was removed")
                    case STATUSES.UNCHANGED:
                        continue
                    case STATUSES.UPDATED:
                        result.append(
                            f"Property '{current_path}' was updated. "
                            f"From {format_value(val[OLD_VALUE])} "
                            f"to {format_value(val[NEW_VALUE])}"
                        )
                    case STATUSES.NESTED:
                        result.append(_iter_plain(val[VALUE], current_path))
                    case _:
                        result.append(_iter_plain(val, current_path))
            else:
                result.append(
                    f"Property '{current_path}' "
                    f"has an unexpected value: {format_value(val)}"
                )
        return "\n".join(result)
    return _iter_plain(diff)
