from model.watcher_model import WatcherModel
from PyQt5.QtCore import QObject, pyqtSlot


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
        print(value)
        self._model.enable_init = value
        self._model.btn_init_text = "Iniciar" if value else "Terminar"
