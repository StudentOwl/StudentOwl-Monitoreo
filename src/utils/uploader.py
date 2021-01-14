from configparser import Error
from urllib3.exceptions import MaxRetryError, NewConnectionError, RequestError
from requests.exceptions import ConnectionError
import json
import requests
from requests import Request, Response

def readFile(pathFile: str) -> str:
    file = ""
    with open(pathFile, "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            file += line
    return file

def verifyServer(server: str) -> bool:
    try:
        pass
    except RequestError as err:
        pass

def main():
    file = readFile("./resources/pruebajson.json")
    # jsonStr = json.loads(file)
    # print(jsonStr)
    try:
        res = requests.get("http://localhost:3000/")
        print(res.text)
    except ConnectionError or MaxRetryError or NewConnectionError as err:
        print("Servidor no disponible")


if __name__ == "__main__":
    main()