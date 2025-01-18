import argparse
import json


def read_and_pars():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('--file', help='specify the path to the JSON file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(json.load(open(args.file)))
