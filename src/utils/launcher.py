import os
import subprocess
from globals import PATH_LAUNCH

class LauncherKidLogger(object):
    """
    Launcher KidLogger Class
    """

    def __init__(self, *args, **kwargs) -> None:  
        self._args = args
        self._kwargs = kwargs
        self._path_launch = PATH_LAUNCH

    def launch (self):
        """
        Metodo con el que inicia el arranque de KidLogger
        """
        subprocess.Popen([PATH_LAUNCH + 'kidlogger_user.exe'])

    
    


