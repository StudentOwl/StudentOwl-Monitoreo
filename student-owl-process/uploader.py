#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import Error
from globals import API_URI_LOGS, LOG_OUTPUT_FILE, LOG_OUTPUT_FOLDER
from urllib3.exceptions import RequestError
from requests.exceptions import ConnectionError
import json
import requests
import os

LOG_FILE = LOG_OUTPUT_FILE
SERVER = API_URI_LOGS
OUT_FILE = os.path.join(LOG_OUTPUT_FOLDER, LOG_OUTPUT_FILE)


def readJsonFile(pathFile: str) -> str:
    file = ""
    with open(pathFile, "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            file += line
    return file


def verifyServer(server: str) -> bool:
    """
    Metodo que verifica que el servidor se encuentre online
    """
    res = None
    try:
        res = requests.get(f"{server}ping")
        print(f"[ALERT]: Ping correct")
    except RequestError as err:
        print("[ERROR]: Server don't response")

    return res.status_code == 200


def uploadLog(url: str, payload) -> bool:
    """
    Metodo que realiza la subida de informacion a la API
    """

    options = {"url": url}

    options["json"] = payload

    res = None
    try:
        res = requests.post(**options)
        print("[ALERT]: POST API")
    except RequestError as err:
        print("[ERROR]: Error uploading information.")

    if res.status_code == 201:
        resjson = res.json()
        print(f"[ALERT]: Response: {resjson['data']}")
        return True
    else:
        print(f"[ERROR]: {res.status_code} {res.content}")

    return False


def main():
    """
    Ejecucion inicial del modulo *provisional*
    """
    file = json.loads(readJsonFile(OUT_FILE))
    payload = file
    if verifyServer(SERVER):
        res = uploadLog(f"{SERVER}logs/new", payload)

        if res:
            print("[INFO]: Exitoso")
        else:
            print("[ERROR]: Error")


if __name__ == "__main__":
    main()
