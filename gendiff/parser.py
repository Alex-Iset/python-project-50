import argparse

from gendiff import diff, load_json, load_yaml


def read_and_pars():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        '--jfile',
        help='specify the path to the JSON file'
    )
    parser.add_argument(
        '-j',
        '--jdiff',
        nargs=2,
        help='specify 2 JSON files to get the difference between them'
    )
    parser.add_argument(
    '--yfile',
    help='specify the path to the YAML file'
    )
    parser.add_argument(
        '-y',
        '--ydiff',
        nargs=2,
        help='specify 2 YAML files to get the difference between them'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    if args.jfile:
        print(load_json(args.jfile))
    elif args.yfile:
        print(load_yaml(args.yfile))
    elif args.jdiff:
        arg1, arg2 = args.jdiff
        print(diff(load_json(arg1), load_json(arg2)))
    elif args.ydiff:
        arg1, arg2 = args.ydiff
        print(diff(load_yaml(arg1), load_yaml(arg2)))
