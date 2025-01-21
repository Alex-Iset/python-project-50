from gendiff.utils import load_supp_file_form


def gen_diff_str(key, value, prefix):
    return f'{prefix} {key}: {value}'


def generate_diff(path_file1, path_file2):
    dict1, dict2 = (
        load_supp_file_form(path_file1),
        load_supp_file_form(path_file2)
    )
    uniq_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = []
    for key in uniq_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result.append(gen_diff_str(key, dict1[key], ' '))
            else:
                result.append(gen_diff_str(key, dict1[key], '-'))
                result.append(gen_diff_str(key, dict2[key], '+'))
        elif key in dict1:
            result.append(gen_diff_str(key, dict1[key], '-'))
        else:
            result.append(gen_diff_str(key, dict2[key], '+'))
    return '{\n' + "\n".join(result) + '\n}'
