#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import getConfigs
from os import path
from time_utils import getDayInInt, getDayInText, getMonthInText

"""
Globals module
Provides all globals varibles for StudentOwl - Watcher.
"""

__version__ = '0.1.0'

# Root Privates
# __ROOT_DIR = path.dirname(path.join('..', path.abspath(__file__)))
__ROOT_DIR = path.dirname('C:/Program Files/StudentOwl/')
__CONFIG_FILE_NAME = 'config.ini'
# print(__ROOT_DIR)
# print(f"Reader: {__ROOT_DIR} | {__CONFIG_FILE_NAME}")


# Print config
configs = getConfigs(path.join(__ROOT_DIR, __CONFIG_FILE_NAME))
for section in configs:
    print(section)
    # print(configs[section])

    for option, value in configs[section].items():
        print(f"\t{option} = {value}")

print('\n')


# More Privates
__dbConfig = getConfigs(path.join(__ROOT_DIR, __CONFIG_FILE_NAME))['db']
__pathConfig = getConfigs(path.join(__ROOT_DIR, __CONFIG_FILE_NAME))['logs']
__basicConfig = getConfigs(path.join(__ROOT_DIR, __CONFIG_FILE_NAME))['basic']
__userConfig = getConfigs(path.join(__ROOT_DIR, __CONFIG_FILE_NAME))['user']

__USERNAME = __userConfig.get('Current', 'default')
__COMPONENT = __userConfig.get('Component', 'GNCP99')

__PATH_LOGS = __pathConfig.get(
    'KidLoggerLogFolder', 'C:\Program Files (x86)\KidLogger\logs')
__LOG_FILE_FORMAT = '{day} {month},{daytext}.htm'
__TEMP_FOLDER_NAME = __pathConfig.get('LogOutputFolder', 'logs')
__LOG_FILE_NAME_OUTPUT = __pathConfig.get('LogOutput', 'studentowl-log.json')
__LOG_LAST_LINE = __pathConfig.get('LastLine', 'C:\mount_nfs.cmd')

__PATH_TO_USERNAME = __basicConfig.get('PathToUsername', 'otro')

__API_URI = __dbConfig.get('UrlService', 'localhost:3000')

# Dirs Globals
LOG_FOLDER = path.abspath(__PATH_LOGS)
DIR_PATH = __ROOT_DIR
LOG_NAME = __LOG_FILE_FORMAT.format_map({
    'day': getDayInInt(),
    'month': getMonthInText(),
    'daytext': getDayInText()
})
LOG_PATH = path.join(LOG_FOLDER, __USERNAME, LOG_NAME)
LOG_OUTPUT_FOLDER = path.join(DIR_PATH, __TEMP_FOLDER_NAME)
LOG_OUTPUT_FILE = __LOG_FILE_NAME_OUTPUT
LOG_LAST_LINE = int(__LOG_LAST_LINE)
CONFIG_FILE_PATH = path.join(__ROOT_DIR, __CONFIG_FILE_NAME)

PATH_TO_USERNAME = path.join('C:', __PATH_TO_USERNAME)

# User Globals
USERNAME = __USERNAME
COMPONENT = __COMPONENT

API_URI_LOGS = __API_URI
