#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from os import path


class Configuration(object):
    """
    Class to represent a configuration file
    """

    def __init__(self, pathfile: str) -> None:
        self._config = ConfigParser()
        self._config.read(path.abspath(pathfile))

    def getConfig(self) -> ConfigParser:
        """
        config property.
        """
        return self._config

    def getSections(self) -> list[str]:
        return self._config.sections()
