from model.watcher_model import WatcherModel
from controllers.watcher_controller import WatcherController
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.watcher_view_ui import WatcherMainWindow


class WatcherView(QMainWindow):
    """
    Watcher main view
    """

    def __init__(self, model: WatcherModel, controller: WatcherController):
        """
        Constructor
        """
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = WatcherMainWindow()
        self._ui.setupUi(self)

        # Variables adicionales
        self.__colorActive = "rgb(102, 105, 197)"
        self.__colorDeactive = "rgb(255, 29, 21)"
        self._styleBtnInit = "background-color: {};\nborder-radius: 8;\ncolor: rgb(255, 255, 255);"

        # connect ui-widget to controller
        # if ui changes, it sends a signal to an slot on which we connect a controller class.
        # therefore we can recive the signal in the controller
        self._ui.cbxComponent.currentIndexChanged.connect(
            self._controller.change_component)
        self._ui.btnInit.clicked.connect(
            lambda: self._controller.change_enable_init(not self._model.enable_init))
        # Lambda to execute function with value
        self._ui.btnInit.clicked.connect(
            lambda: self._controller.change_run_timer(not self._model.isRunTimer))
        #Launch KidLogger tool
        self._ui.btnInit.clicked.connect(
            lambda: self._controller.launch_kidlogger(not self._model.launcherKidLogger))
        # listen for model event signals
        # connect the method to update the ui to the slots of the model
        # if model sends/emits a signal the ui gets notified
        self._model.name_changed.connect(self.on_name_changed)
        self._model.enable_init_changed.connect(self.on_enable_init_changed)
        self._model.init_text_changed.connect(self.on_text_init_changed)
        self._model.component_changed.connect(self.on_component_changed)
        self._model.components_changed.connect(
            self.on_combo_components_changed)

        # set a default value
        self._controller.change_component(0)
        self._ui.cbxComponent.addItems(self._model.get_components_names())

    @pyqtSlot(str)
    def on_name_changed(self, value):
        self._ui.lblStudentName.setText(value)

    @pyqtSlot(int)
    def on_component_changed(self, value):
        self._ui.cbxComponent.setCurrentIndex(value)

    @pyqtSlot(bool)
    def on_enable_init_changed(self, value):
        # self._ui.btnInit.setEnabled(value)
        self._ui.btnInit.setStyleSheet(
            self._styleBtnInit.format(self.__colorActive if value else self.__colorDeactive))

    @pyqtSlot(str)
    def on_text_init_changed(self, value):
        self._ui.btnInit.setText(value)

    @pyqtSlot(list)
    def on_combo_components_changed(self, value):
        self._ui.cbxComponent.clear()
        self._ui.cbxComponent.addItems(value)
"""
    @pyqtSlot(bool)
    def on_launch(self, value):
        self._ui.btnInit.start
"""