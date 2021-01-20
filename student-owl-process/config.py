#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

"""
Config module
Provides methods for obtaining config parameters.
"""

__version__ = '0.1.0'


def getConfigs(pathfile: str) -> ConfigParser:
    """
    Metodo que permite acceder a las configuraciones 
    dentreo de un archivo `.ini`
    """
    config = ConfigParser()
    config.read(pathfile)
    print(f"[ACCESS]: Access to: {pathfile}")
    return config


def writeConfigs(pathfile: str, options: dict[str, dict[str, object]]) -> ConfigParser:
    """
    docstring
    """
    config = ConfigParser()
    # config.read(pathfile)

    for section in options:
        if not config.has_section(section):
            config.add_section(section)

        for option, value in options[section].items():
            config.set(section, option, value)

    config.write(open(pathfile, mode="w", encoding="utf8"))


def updateConfigs(pathfile: str, options: dict[str, dict[str, object]]) -> ConfigParser:
    """
    docstring
    """

    config = ConfigParser()
    config.read(pathfile)

    for section in options:
        if not config.has_section(section):
            config.add_section(section)

        for option, value in options[section].items():
            config.set(section, option, str(value))

    config.write(open(pathfile, mode="w", encoding="utf8"))
