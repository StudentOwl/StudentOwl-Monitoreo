from model.watcher_model import WatcherModel
from PyQt5.QtCore import QObject, pyqtSlot
from utils.launcher import LauncherKidLogger

class WatcherController(QObject):
    """
    Controller for Watcher View
    """

    def __init__(self, model: WatcherModel):
        """
        Constructor de clase
        """
        super().__init__()

        self._model = model

    # Takes Signal from UI
    @pyqtSlot(int)
    def change_component(self, value):
        """
        Evento de cambio de componente academico
        """
        self._model.component_selected = value

    @pyqtSlot(bool)
    def change_enable_init(self, value):
        """
        Evento que modifica el boton de inicio
        """
        self._model.enable_init = value
        self._model.btn_init_text = "Iniciar" if value else "Terminar"

    @pyqtSlot(bool)
    def launch_kidlogger(self, value):
        """
        Evento que inicia con la herramienta KidLogger
        """        
        self._model.launcherKidLogger = value
        self._model.runKidLogger()
        #self._model.stopKidLogger()
        
    def change_run_timer(self, value):
        """
        Evento que activa el TimerThread
        """
        self._model.isRunTimer = value
        self._model.runTimer()
        self._model.stopTimer()
