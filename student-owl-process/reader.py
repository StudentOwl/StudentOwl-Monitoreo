#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from time_utils import convertTimeToTimestamp
from globals import CONFIG_FILE_PATH, LOG_LAST_LINE, LOG_OUTPUT_FOLDER, LOG_PATH, USERNAME, COMPONENT, LOG_OUTPUT_FILE
from config import updateConfigs

"""
Reader module
Provides methods for obtaining log registers and write new logs in JSON format.
"""

__version__ = '0.1.0'

__EXCLUDED_CLASSES = ('system', 'clipboard', 'url', 'keystrokes', 'jpg',)
__ACCEPTED_CLASSES = ('app')

__PATHFILE = LOG_PATH
__OUT_FOLDER = LOG_OUTPUT_FOLDER
__OUT_FILE = os.path.join(__OUT_FOLDER, LOG_OUTPUT_FILE)

__lastLine = LOG_LAST_LINE


def getLines() -> list[str]:
    """
    Metodo que devuelve una lista de lineas
    """
    lines = []
    pastLastLine = __lastLine
    newLastLine = pastLastLine

    with open(__PATHFILE, 'r', encoding='utf8') as file:
        lines = file.readlines()
        newLastLine = len(lines)

    updateConfigs(CONFIG_FILE_PATH, {"logs": {"LastLine": newLastLine}})

    lines = lines[pastLastLine:]

    return lines


def proccessJson(jsonData: dict) -> dict:
    if jsonData["class"] in __ACCEPTED_CLASSES:
        if jsonData.get("duration"):
            jsonData["duration"] = int(jsonData["duration"])
        if jsonData.get("time"):
            jsonData["time"] = convertTimeToTimestamp(jsonData["time"])*1000

        jsonData["student"] = USERNAME
        jsonData["component"] = COMPONENT

        return jsonData
    else:
        return None


def getJson(lines: list[str]) -> list[dict]:
    """
    Metodo que procesa las lineas de texto a JSON
    """
    logs = []
    print("[ALERT]: Init process JSON")
    for line in lines:
        if line.strip() != "":
            line = line.replace(',\n', '').replace('\\', '\\\\')
            try:
                line: dict = json.loads(line)
                if type(line) == dict:
                    line = proccessJson(line)
                    if line:
                        logs.append(line)
                else:
                    print("[ERROR]: Not a dict")
            except ValueError as err:
                print("[ERROR]: Not a valid JSON")
                print(f"\t{err}")
                print(f"\t{line}")
    print("[ALERT]: End process JSON")

    # return json.dumps(logs) if len(logs) > 0 else None
    return logs


def writeJsonFile(path, values) -> None:
    try:
        os.mkdir(__OUT_FOLDER)
    except FileExistsError as err:
        print(f"[ALERT]: '{__OUT_FOLDER}' folder exists")

    with open(path, 'w') as file:
        json.dump(values, file)


def main():
    lines = getLines()
    jsonLines = getJson(lines)
    writeJsonFile(__OUT_FILE, jsonLines)


if __name__ == "__main__":
    main()
