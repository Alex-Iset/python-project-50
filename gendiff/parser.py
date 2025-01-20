import argparse

from gendiff import diff, load_json


def read_and_pars():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        '--file',
        help='specify the path to the JSON file'
    )
    parser.add_argument(
        '-d',
        '--diff',
        nargs=2,
        help='specify 2 JSON files to get the difference between them'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    if args.file:
        print(load_json(args.file))
    if args.diff:
        arg1, arg2 = args.diff
        print(diff(load_json(arg1), load_json(arg2)))
