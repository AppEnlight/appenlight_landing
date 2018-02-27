#!/usr/bin/env python3

import subprocess
import os
import argparse
import shutil
import tempfile

env = os.environ.copy()

parser = argparse.ArgumentParser(description='Build static application')
args = parser.parse_args()

dir_cwd = os.path.dirname(os.path.realpath(__file__))

install_path = tempfile.mkdtemp()

env['PYTHONPATH'] = install_path
args = ['python3', 'setup.py', 'develop',
        '--install-dir={}'.format(install_path)]

try:
    subprocess.Popen(args, cwd=os.path.join(dir_cwd, 'backend'), env=env).communicate()
    args = [os.path.join(install_path, 'pserve'), 'production.ini']
    proc = subprocess.Popen(args, env=env)
    try:
        proc.communicate(timeout=3)
    except subprocess.TimeoutExpired:
        pass
    print('ok use wget')
    try:
        os.mkdir('build')
    except Exception:
        pass
    args = ['wget',
            '--recursive',
            '--page-requisites',
            '--convert-links',
            '--no-host-directories',
            '--domains', '127.0.0.1',
            '--html-extension',
            '--directory-prefix=build',
            'http://127.0.0.1:20000'
        ]
    subprocess.call(args)
    proc.kill()
finally:
    shutil.rmtree(install_path)
