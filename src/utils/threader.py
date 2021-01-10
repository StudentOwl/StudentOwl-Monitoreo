#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Timer


class RepeatedTimer(object):
    """
    An class to implement the running periodically function
    """

    def __init__(self, interval: int, theFunction: function, *args, **kwargs) -> None:
        self._timer = None
        self._interval = interval
        self._theFunction = theFunction
        self._args = args
        self._kwargs = kwargs
        self._is_running = False
        self.start()

    def _run(self):
        self._is_running = False
        self.start()
        self._theFunction(*self._args, **self._kwargs)

    def start(self):
        if not self._is_running:
            self._timer = Timer(self._interval, self._run)
            self._timer.start()
            self._is_running = True

    def stop(self):
        self._timer.cancel()
        self._is_running = False
