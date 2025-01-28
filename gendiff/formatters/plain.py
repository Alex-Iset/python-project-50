from gendiff.consts import NEW_VALUE, OLD_VALUE, VALUE


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff, path=""):
    result = []

    for key, val in diff.items():
        current_path = f"{path}.{key}" if path else key

        if isinstance(val, dict) and "added" in val.values():
            result.append(
                f"Property '{current_path}' "
                f"was added with value: {format_value(val[VALUE])}"
            )
        elif isinstance(val, dict) and "removed" in val.values():
            result.append(f"Property '{current_path}' was removed")
        elif isinstance(val, dict) and "unchanged" in val.values():
            continue
        elif isinstance(val, dict) and "changed" in val.values():
            result.append(
                f"Property '{current_path}' was updated. "
                f"From {format_value(val[OLD_VALUE])} "
                f"to {format_value(val[NEW_VALUE])}"
            )
        elif isinstance(val, dict) and "nested" in val.values():
            result.append(plain(val[VALUE], current_path))
        elif isinstance(val, dict):
            result.append(plain(val, current_path))
        else:
            result.append(
                f"Property '{current_path}' "
                f"has an unexpected value: {format_value(val)}"
            )

    return "\n".join(result)
