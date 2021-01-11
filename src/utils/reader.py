#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from os import path

from utils.time_utils import convertTimeToTimestamp


class ReaderLogFile(object):
    """
    Reader LogFile class
    Provides methods for obtaining log lines.
    """

    __EXCLUDED_CLASSES = ('system', 'clipboard', 'url', 'keystrokes', 'jpg',)
    __ACCEPTED_CLASSES = ('app')

    def __init__(self, pathfile: str, lastLine=0):
        """
        Constructor de clase
        """
        self._pathfile = path.abspath(pathfile)
        self.lastLine = lastLine

    def getLines(self) -> list[str]:
        """
        Metodo que devuelve una lista de lineas
        """
        lines = []
        pastLastLine = self.lastLine
        with open(self._pathfile, 'r', encoding='utf8') as file:
            # file.seek(self.lastLine,0)
            lines = file.readlines()
            self.lastLine = len(lines)
        lines = lines[pastLastLine:]

        return lines

    def getJson(self, lines: list[str]) -> str:
        """
        Metodo que procesa las lineas de texto a JSON
        """
        logs = []
        for line in lines:
            if line.strip() != "":
                line = line.replace(',\n', '').replace('\\', '\\\\')
                try:
                    line: dict = json.loads(line)
                    if type(line) == dict:
                        line = self.proccessJson(line)
                        if line:
                            logs.append(line)
                    else:
                        print("[ERROR]: Not a dict")
                except ValueError as err:
                    print("[ERROR]: Not a valid JSON")
                    print(f"\t{err}")
                    print(f"\t{line}")

        return json.dumps(logs) if len(logs) > 0 else None

    def proccessJson(self, jsonData: dict) -> dict:
        if jsonData["class"] in self.__ACCEPTED_CLASSES:
            if jsonData.get("duration"):
                jsonData["duration"] = int(jsonData["duration"])
            if jsonData.get("time"):
                jsonData["time"] = convertTimeToTimestamp(jsonData["time"])

            return jsonData
        else:
            return None
