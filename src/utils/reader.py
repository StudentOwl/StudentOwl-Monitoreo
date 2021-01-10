#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from os import path
from utils.config import Configuration
import time

config = Configuration("config.ini").getConfig()


# def followFile(thisfile: io.TextIOWrapper):
#     """
#     Generator to read file
#     """
#     thisfile.seek(0, 2)
#     while True:
#         line = thisfile.readline()
#         if not line:
#             time.sleep(3)
#             continue
#         yield line


def followFile(thisfile: io.TextIOWrapper):
    """
    Generator to read file
    """
    thisfile.seek(0, 2)
    while True:
        line = thisfile.readline()
        if not line:
            time.sleep(3)
            continue
        yield line


def main():
    """
    Main function
    """
    pathfile = path.join(config['log.options']['path'],
                         config['log.options']['user'], "8 January,Friday.htm")
    logfile = open(pathfile, "r")
    loglines = followFile(logfile)

    for line in loglines:
        print(line)


if __name__ == "__main__":
    main()
