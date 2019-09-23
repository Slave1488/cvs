import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t",
                        action="store",
                        nargs=,
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
