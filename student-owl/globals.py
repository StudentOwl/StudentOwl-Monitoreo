#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from utils.config import Configuration
from utils.time_utils import getDayInInt, getDayInText, getMonthInText

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.ini')

__config = Configuration(CONFIG_PATH).config

# Globals
# Log Constants
PATH_LOGS_FOLDER = __config['log.options']['path']
USER_NAME = __config['log.options']['user']
__LOG_FILE_FORMAT = __config['log.options']['format.file']
LOG_NAME = __LOG_FILE_FORMAT.format_map(
    {'day': getDayInInt(), 'month': getMonthInText(), 'daytext': getDayInText()})
LOG_PATH = f"{PATH_LOGS_FOLDER}\\{USER_NAME}\\{LOG_NAME}"
