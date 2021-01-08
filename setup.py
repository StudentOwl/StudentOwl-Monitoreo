from os import name
from setuptools import setup, find_packages

setup(
    name='StudentOwl - Monitoreo',
    version='1.0',
    description='Modulo de recopilación de información de StudentOwl',
    author='Juan Gahona',
    author_email='gahonajuanjo@gmail.com',
    install_requires=['pyqt5', 'pytest'],
    url='https://github.com/StudentOwl/StudentOwl-Monitoreo.git',
    license=license,
    packges=find_packages(exclude=('tests'))
)
