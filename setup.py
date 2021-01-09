#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import setup, find_packages

setup(
    name='StudentOwl - Monitoreo',
    version='1.0',
    license=license,
    description='Modulo de recopilación de información de StudentOwl',
    author='Juan Gahona',
    author_email='gahonajuanjo@gmail.com',
    url='https://github.com/StudentOwl/StudentOwl-Monitoreo.git',

    packages=find_packages('src', exclude=('tests')),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,

    install_requires=['pyqt5', 'pytest'],
)
