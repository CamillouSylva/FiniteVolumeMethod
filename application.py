# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from FiniteVolumeMethod.Model.model_data import Model
from FiniteVolumeMethod.View.main_view import MainView
from FiniteVolumeMethod.Controller.controller import MainController


class Application(QApplication):
    def __init__(self, sys_argv):
        super(Application, self).__init__(sys_argv)

        # Connecter tout ensemble
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()


if __name__ == '__main__':
    app = Application(sys.argv)
    sys.exit(app.exec_())
