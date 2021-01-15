from configparser import Error
from requests.api import options
from urllib3.exceptions import MaxRetryError, NewConnectionError, RequestError
from requests.exceptions import ConnectionError
import json
import requests
from requests import Request, Response


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
        res = requests.get(server)
    except RequestError as err:
        print("[ERROR]: Server don't response")

    if res:
        return res.status_code == 200

    return False


def uploadLog(url: str, payload) -> bool:
    """
    Metodo que realiza la subida de informacion a la API
    """

    options = {"url": url}

    if type(payload) == dict or type(payload) == list:
        options["json"] = payload
    elif type(payload) == str:
        options["data"] = payload
    else:
        return False

    res = None
    try:
        res = requests.post(**options)
    except RequestError as err:
        print("[ERROR]: Error uploading information.")

    if res:
        resjson = res.json()
        print(resjson["message"])
        return True
    else:
        print(res.status_code)

    return False


def main():
    file = readJsonFile("./resources/pruebajson.json")
    file = json.loads(file)
    payload = {"count":len(file), "data": file}
    server = "http://localhost:3000/"
    route = "api/v1.0/GSPR01/lfbermeo"
    
    if verifyServer(server):
        res = uploadLog(f"{server}{route}", payload)

        if res:
            print("[INFO]: Exitoso")
        else:
            print("[ERROR]: Error")


if __name__ == "__main__":
    main()
