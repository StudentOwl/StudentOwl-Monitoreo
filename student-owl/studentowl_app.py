import sys
from PyQt5.QtWidgets import QApplication
from model.watcher_model import WatcherModel
from controllers.watcher_controller import WatcherController
from views.watcher_view import WatcherView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Connect everything together
        self.model = WatcherModel()
        self.main_ctrl = WatcherController(self.model)
        self.main_view = WatcherView(self.model, self.main_ctrl)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
