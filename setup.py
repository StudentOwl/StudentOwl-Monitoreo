#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

packages = ['src', 'src.controllers', 'src.model', 'src.utils', 'src.views']

packages_data = {'': ['*'], 'src': ['resources/*', 'resources/img/']}

install_requires = ['PyQt5>=5.15.2,<6.0.0']

setup_kwargs = {
    'name': 'studentowl-watcher',
    'version': '0.1.0',
    'description': '',
    'long_description': 'Proyecto de reto',
    'author': 'Scoowy',
    'author_email': 'gahonajuanjo@gmail.com',
    'maintainer': None,
    'maintainer_email': 'None',
    'url': 'https://github.com/StudentOwl/StudentOwl-Monitoreo.git',
    'packages': packages,
    'packages_data': packages_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}

setup(**setup_kwargs)
