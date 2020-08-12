#!/usr/bin/env python3

'''
This script does a major task:  take in several options and create a working balsam

Options:
Python
  - if passed, use this python and build a virtual env
  - if empty, fetch the latest conda and get that python, then build a virtualenv
Software location
  - if passed, install software within this directory.
  - if empty, install software in a timestamp-named directory under /projects/datascience/balsam-ci
'''

import sys, os
import argparse
import pathlib
import subprocess

def init_database(dir_path : pathlib.Path):
    command = '''
        source {dir_path}/software/setup.sh
    '''

def main():


    parser = argparse.ArgumentParser(
        description='Initialize database for balsam',
        usage='''software_deps.py [<args>]''',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('--directory',
        help="Top level location for this installation",
        type=pathlib.Path)

    args = parser.parse_args()


    # First, create the directory:
    create_directory(args.directory)

    # Next, create a virtual env within that directory:
    build_env(args.directory / pathlib.Path("env"), args.python)

    install_balsam(args.directory / pathlib.Path("env"))

    write_setup_script(args.directory)

if __name__ == '__main__':
    main()
