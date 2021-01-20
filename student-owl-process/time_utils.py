#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, datetime

"""
Time utils module
Provides methods for convert times.
"""

__version__ = '0.1.0'

__months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
            7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
__days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
          4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


def getDayInInt() -> int:
    """
    Metodo que retorna el dia actual en numero `0...31`
    """
    today = date.today()
    return today.day


def getDayInText() -> str:
    """
    Metodo que retorna el dia actual en texto.
    - `Monday`
    - `Tueday`
    - `Wednesday`
    - `Thursday`
    - `Friday`
    - `Saturday`
    - `Sunday`
    """
    today = date.today()
    return __days[today.isoweekday()]


def getMonthInText() -> str:
    """
    Metodo que retorna el mes actual
    `January...December`
    """
    today = date.today()
    return __months[today.month]


def convertTimeToTimestamp(timeStr: str):
    """
    Convert time HH:MM:SS -> ISOTime YYYY-mm-ddTHH:MM:SS.f

    Toma la fecha actual para completar la informacion.
    - Example: 12:21:47 -> 2021-01-10T12:21:47.000000
    - Example: 12:21:47.4751 -> 2021-01-10T12:21:47.475100
    """
    timeTuple = timeStr.split(':')
    timeStrISO = f"{timeTuple[0]}:{timeTuple[1]}:{timeTuple[2]}"
    if len(timeTuple) == 4:
        timeStrISO += ".{:0<6}".format(timeTuple[3])

    fecha = datetime.fromisoformat(f"{date.today().isoformat()}T{timeStrISO}")
    return fecha.timestamp()
