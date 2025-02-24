from gendiff.consts import NEW_VALUE, OLD_VALUE, STATUS, VALUE


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
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

    def format_line(indent, key, value):
        return f"{indent}{key}: {stylish(value, deep_indent)}"

    result = []
    for key, val in diff.items():
        if isinstance(val, dict):
            status = val.get(STATUS)
            match status:
                case "added":
                    result.append(
                        format_line(form_indent["add"], key, val[VALUE])
                    )
                case "removed":
                    result.append(
                        format_line(form_indent["remove"], key, val[VALUE])
                    )
                case "unchanged":
                    result.append(
                        format_line(form_indent["empty"], key, val[VALUE])
                    )
                case "changed":
                    result.append(
                        format_line(form_indent["remove"], key, val[OLD_VALUE])
                    )
                    result.append(
                        format_line(form_indent["add"], key, val[NEW_VALUE])
                    )
                case "nested":
                    result.append(
                        format_line(new_deep_indent, key, val[VALUE])
                    )
                case _:
                    result.append(
                        format_line(new_deep_indent, key, val)
                    )
        else:
            result.append(
                format_line(new_deep_indent, key, val)
            )
    return "{\n" + "\n".join(result) + "\n" + current_deep + "}"
