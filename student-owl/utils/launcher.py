import os

class LauncherKidLogger(object):
    """
    Launcher KidLogger Class
    """

    def launch (self):
        """
        Metodo con el que inicia el arranque de KidLogger
        """
        path = ""
        os.system(path + 'kidlogger_user.exe')
