#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.config import Configuration
from utils.time_utils import getDayInInt, getDayInText, getMonthInText

__config = Configuration("config.ini").config

# Globals
# Log Constants
PATH_LOGS_FOLDER = __config['log.options']['path']
USER_NAME = __config['log.options']['user']
LOG_FILE_FORMAT = __config['log.options']['format.file']
LOG_NAME = LOG_FILE_FORMAT.format_map(
    {'day': getDayInInt(), 'month': getMonthInText(), 'daytext': getDayInText()})
