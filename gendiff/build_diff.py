from gendiff.consts import NEW_VALUE, OLD_VALUE, STATUS, STATUSES, VALUE


def build_diff(dict1, dict2):
    uniq_keys = sorted(dict1.keys() | dict2.keys())

    diff_dict = {}

    for key in uniq_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict1:
            diff_dict[key] = {
                STATUS: STATUSES.ADDED,
                VALUE: value2
            }
        elif key not in dict2:
            diff_dict[key] = {
                STATUS: STATUSES.REMOVED,
                VALUE: value1
            }
        elif value1 == value2:
            diff_dict[key] = {
                STATUS: STATUSES.UNCHANGED,
                VALUE: value1
            }
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff_dict[key] = {
                STATUS: STATUSES.NESTED,
                VALUE: build_diff(value1, value2)
            }
        else:
            diff_dict[key] = {
                STATUS: STATUSES.UPDATED,
                OLD_VALUE: value1,
                NEW_VALUE: value2
            }
    return diff_dict
