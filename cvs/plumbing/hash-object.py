#!/usr/bin/env python3

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t",
                        action="store",
                        nargs=1,
                        const=,
                        default=,
                        type=,
                        choices=,
                        required=,
                        help="object type",
                        dest="type",
                        metavar="<type>")
    parser.add_argument("-w",
                        action="store_true",
                        help="write the object into the object database")
    parser.add_argument("<file>", nargs='+',
                        help="help")
    return parser.parse_args()


def main():
    args = parse_args()
    print(args)

if __name__ == "__main__":
    main()
