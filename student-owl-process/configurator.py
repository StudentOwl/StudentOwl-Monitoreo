#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from globals import PATH_TO_USERNAME, CONFIG_FILE_PATH
from config import updateConfigs

"""
Configurator module
Provides methods for obtaining log registers and write new logs in JSON format.
"""

__version__ = '0.1.0'


def getStudent():
    pattern = re.compile(r'\/mnt\/UTPL\/(\w+) \*')
    with open(PATH_TO_USERNAME) as file:
        line = file.readlines()[-1]
        match = re.findall(pattern, line)

    return match[0]


def main():
    username = getStudent()
    print(f"[ALERT]: Username: {username}")
    updateConfigs(CONFIG_FILE_PATH, {"user": {"Current": username}})


if __name__ == "__main__":
    main()
