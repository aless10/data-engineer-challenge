# -*- coding: utf-8 -*-
"""
Data Engineer Challenge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from __future__ import absolute_import

import sys
from setuptools import setup, find_packages
from pkg_resources import parse_requirements

with open("requirements.txt".format(*sys.version_info[0:2]), 'r') as inst_reqs:
    install_requires = [str(req) for req in parse_requirements(inst_reqs)]

packages = find_packages(include=['src', 'src.*'])

setup(
    name='DataEngineerChallenge',
    version='0.1.0-dev',
    url='https://github.com/aless10/data-engineer-challenge',
    license='LICENSE.txt',
    author='Alessio Izzo',
    author_email='alessio.izzo86@gmail.com',
    description='A challenge to become a data engineer',
    long_description=__doc__,
    packages=packages,
    install_requires=install_requires,
    include_package_data=True,
)
