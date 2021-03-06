from globals import LOG_PATH
from PyQt5.QtCore import QObject, pyqtSignal
from utils.reader import ReaderLogFile
from utils.threader import RepeatedTimer

from model.models import Component


class WatcherModel(QObject):
    """
    Model for Watcher View
    """
    component_changed = pyqtSignal(int)
    components_changed = pyqtSignal(list)
    enable_init_changed = pyqtSignal(bool)
    name_changed = pyqtSignal(str)
    init_text_changed = pyqtSignal(str)
    launch_tool = pyqtSignal(bool)

    is_run_timer_changed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self._components = [
            Component("COM-GP-A", "Gestion de proyectos",  "A"),
            Component("COM-GP-B", "Gestion de proyectos",  "B"),
            Component("COM-IR-A", "Ingenieria de requisitos",  "A"),
        ]
        self._student_name = ''
        self._component_selected = -1
        self._enable_init = True
        self._btn_init_text = "Iniciar"
        self._enable_launcher = False

        self._isRunTimer = False

        self._timer = RepeatedTimer(15, self.funtionRepeat)

        self._reader = ReaderLogFile(LOG_PATH)

    @property
    def components(self) -> list[dict[str, str]]:
        """
        Propiedad que contiene los componentes academicos.
        """
        return self._components

    @components.setter
    def components(self, value):
        self._components = value
        self.components_changed.emit(self._components)

    def add_component(self, value):
        """
        Metodo que aniade un nuevo componente academico.
        """
        self._components.append(value)
        self.components_changed.emit(self._components)

    def get_components_names(self):
        """
        Metodo que devuelve una lista de nombre de los compomentes academicos
        """
        return list(map(lambda comp: comp.__str__(), self._components))

    @property
    def student_name(self) -> str:
        """
        Propiedad que contiene el nombre del estudiante
        """
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value
        self.name_changed.emit(self._student_name)

    @property
    def component_selected(self) -> int:
        """
        component_selected property.
        """
        return self._component_selected

    @component_selected.setter
    def component_selected(self, value):
        self._component_selected = value
        self.component_changed.emit(self._component_selected)

    @property
    def enable_init(self) -> bool:
        """
        enable_init property.
        """
        return self._enable_init

    @enable_init.setter
    def enable_init(self, value):
        self._enable_init = value
        self.enable_init_changed.emit(self._enable_init)

    @property
    def btn_init_text(self) -> str:
        """
        btn_init_text property.
        """
        return self._btn_init_text

    @btn_init_text.setter
    def btn_init_text(self, value):
        self._btn_init_text = value
        self.init_text_changed.emit(self._btn_init_text)

    @property
    def isRunTimer(self) -> bool:
        """
        isRunningTimer property.
        """
        return self._isRunTimer

    @isRunTimer.setter
    def isRunTimer(self, value):
        self._isRunTimer = value
        self.is_run_timer_changed.emit(self._isRunTimer)

    def runTimer(self):
        """
        Method to implement TimerThread functionality
        """
        if self._isRunTimer:
            print("Entro al START")
            self._timer.start()

    def stopTimer(self):
        if not self._isRunTimer:
            print("Entro al STOP")
            self._timer.stop()

    def funtionRepeat(self):
        jsonLogs = self._reader.getJson(self._reader.getLines())
        if jsonLogs != None:
            print(jsonLogs)
        self.student_name = str(self._reader.lastLine)
