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
import time, datetime


def create_directory(dir_path : pathlib.Path):
    # Take a directory location,
    dir_path.mkdir(parents=True, exist_ok=True)

def build_env(env_path : pathlib.Path, python):
    p = subprocess.Popen([python, "-m", "virtualenv", "--system-site-packages", env_path])
    print("Creating virtualenv ... ")
    p.communicate()


def install_mpi4py(virtualenv_path : pathlib.Path):

    # Install balsam and it's dependencies:
    command = f"source {virtualenv_path}/bin/activate; MPICC=CC pip install mpi4py;"
    p = subprocess.Popen(command, shell=True)
    print("Installing mpi4py into the virtualenv")
    p.communicate()

def install_balsam(virtualenv_path : pathlib.Path):

    # Install balsam and it's dependencies:
    command = f"source {virtualenv_path}/bin/activate; pip install balsam;"
    p = subprocess.Popen(command, shell=True)
    print("Installing balsam into the virtualenv")
    p.communicate()

def write_setup_script(dir_path):

    with open(f'{dir_path}/setup_env.sh', 'w') as _f:
        _f.write("#!/bin/bash\n")
        _f.write("\n")
        _f.write(f"source {dir_path}/software/env/activate\n")


def main():

    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')

    parser = argparse.ArgumentParser(
        description='Build software deps for balsam',
        usage='''software_deps.py [<args>]''',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--python',
        help='Use this python to build an exectuable',
        default=sys.executable)
    parser.add_argument('--directory',
        help="Top level location for this installation",
        type=pathlib.Path,
        default=f"/projects/datascience/balsam-ci/{timestamp}/software/")

    args = parser.parse_args()


    # First, create the directory:
    create_directory(args.directory)

    # Next, create a virtual env within that directory:
    build_env(args.directory / pathlib.Path("env"), args.python)

    install_balsam(args.directory / pathlib.Path("env"))

    write_setup_script(args.directory)

if __name__ == '__main__':
    main()
