#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
import shutil

ERROR_EXCEPTION = 1
ERROR_WRONG_SETTINGS = 2
ERROR_PYTHON_VERSION = 3
ERROR_MODULES_MISSING = 4

if sys.version_info < (3, 6):
    print('Use python >= 3.6', file=sys.stderr)
    sys.exit(ERROR_PYTHON_VERSION)

try:
    from cvs import porcelain
except Exception as e:
    print('Cvs module not found: "{}"'.format(e), file=sys.stderr)
    sys.exit(ERROR_MODULES_MISSING)

path_test = Path('W:\\') / 'Py' / 'CVS' / 'Test'

parser = argparse.ArgumentParser(description='MyLitleGit')

subparsers = parser.add_subparsers(help='commands')


class Command:
    name = ''

    def func():
        pass

    def __init__(self, name, func):
        self.name = name
        self.func = func

commands = [
    Command('init',   cvs.init),
    Command('add',    cvs.add),
    Command('commit', cvs.commit),
    Command('reset',  cvs.reset),
    Command('log',    cvs.log)
    ]


def init_subparser(command):
    init_subparser = subparsers.add_parser(command.name)
    init_subparser.set_defaults(func=command.func)
    return init_subparser

parsers = map(init_subparser, commands)

for p in parsers:
    p.add_argument('path',
                   metavar='path',
                   nargs='?', default=path_test,
                   help='path of rep')

args = parser.parse_args()

args.func(args)
