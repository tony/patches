#!/usr/bin/env python

from __future__ import absolute_import, print_function, unicode_literals

import os
import subprocess
import sys


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)


def fail(message):
    sys.exit("Error: {message}".format(message=message))


def has_module(module_name):
    try:
        import imp
        imp.find_module(module_name)
        del imp
        return True
    except ImportError:
        return False


def which(exe=None, throw=True):
    """Return path of bin. Python clone of /usr/bin/which.

    from salt.util - https://www.github.com/saltstack/salt - license apache

    :param exe: Application to search PATHs for.
    :type exe: string
    :param throw: Raise ``Exception`` if not found in paths
    :type throw: bool
    :rtype: string

    """
    if exe:
        if os.access(exe, os.X_OK):
            return exe

        # default path based on busybox's default
        default_path = '/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin'
        search_path = os.environ.get('PATH', default_path)

        for path in search_path.split(os.pathsep):
            full_path = os.path.join(path, exe)
            if os.access(full_path, os.X_OK):
                return full_path

        message = (
            '{0!r} could not be found in the following search '
            'path: {1!r}'.format(
                exe, search_path
            )
        )

        if throw:
            raise Exception(message)
        else:
            print(message)
    return None


project_dir = os.path.dirname(os.path.realpath(__file__))
env_dir = os.path.join(project_dir, '.venv')
pip_bin = os.path.join(env_dir, 'bin', 'pip')
python_bin = os.path.join(env_dir, 'bin', 'python')
virtualenv_bin = which('virtualenv', throw=False)
virtualenv_exists = os.path.exists(env_dir) and os.path.isfile(python_bin)
entr_bin = which('entr', throw=False)
nvim_bin = which('nvim', throw=False)
dev_reqs_fpath = os.path.join(project_dir, 'requirements', 'dev.txt')
test_reqs_fpath = os.path.join(project_dir, 'requirements', 'test.txt')
test27_reqs_fpath = os.path.join(project_dir, 'requirements', 'test-py27.txt')
sphinx_reqs_fpath = os.path.join(project_dir, 'requirements', 'doc.txt')


if not has_module('virtualenv'):
    message = (
        'Virtualenv is required for this bootstrap to run.\n'
        'Install virtualenv via:\n'
        '\t$ [sudo] pip install virtualenv'
    )
    fail(message)


if not has_module('pip'):
    message = (
        'pip is required for this bootstrap to run.\n'
        'Find instructions on how to install at: %s' %
        'http://pip.readthedocs.io/en/latest/installing.html'
    )
    fail(message)


def main():
    if not virtualenv_exists:
        virtualenv_bin = which('virtualenv', throw=False)

        subprocess.check_call(
            [virtualenv_bin, env_dir]
        )

        subprocess.check_call(
            [pip_bin, 'install', '-e', project_dir]
        )

    if not entr_bin:
        message = (
            'entr(1) is missing.\n'
            'If you want to enable rebuilding documentation and '
            're-running commands when a file is saved.\n'
            'See https://bitbucket.org/eradman/entr/'
        )
        print(message)

    # neovim requires this to be installed in the virtualenv 05/13/2016
    if nvim_bin:
        try:
            import neovim  # noqa
        except ImportError:
            subprocess.check_call(
                [pip_bin, 'install', 'neovim']
            )

    try:
        import pytest  # noqa
    except ImportError:
        subprocess.check_call(
            [pip_bin, 'install', '-r', test_reqs_fpath]
        )

    if not os.path.isfile(os.path.join(env_dir, 'bin', 'flake8')):
        subprocess.check_call(
            [pip_bin, 'install', '-r', dev_reqs_fpath]
        )

    if not os.path.isfile(os.path.join(env_dir, 'bin', 'sphinx-quickstart')):
        subprocess.check_call(
            [pip_bin, 'install', '-r', sphinx_reqs_fpath]
        )

    if os.path.exists(os.path.join(env_dir, 'build')):
        os.removedirs(os.path.join(env_dir, 'build'))

if __name__ == '__main__':
    main()
