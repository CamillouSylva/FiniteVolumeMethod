# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtSlot

from FiniteVolumeMethod.Model.model_data import Model
from FiniteVolumeMethod.IHM.model import ModelEditable, Delegate
from FiniteVolumeMethod.Job.W import Wl, Wr


class MainController(QObject):  # QObject est nécessaire pour pouvoir utiliser les @pyqtSlot()
    def __init__(self, model: Model):
        super().__init__()

        self._model = model
        self._model_wl = ModelEditable(data=Wl(self._model.rl, self._model.ul, self._model.pl),
                                       table_header=["r_l", "u_l", "p_l"])
        self._model_wr = ModelEditable(data=Wr(self._model.rr, self._model.ur, self._model.pr),
                                       table_header=["r_r", "u_r", "p_r"])

    @property
    def delegate(self):
        return Delegate(self)

    @pyqtSlot(float)
    def change_l_value(self, value):
        """
        :param value: Nouvelle valeur de L
        :return:
        """
        self._model.L = value
        print("New L : ", value)
        print(self._model)

    @pyqtSlot(int)
    def change_nx_value(self, value):
        self._model.Nx = value
        print("New Nx: ", value)
        print(self._model)

    @pyqtSlot(float)
    def change_cfl_value(self, value):
        self._model.cfl = value
        print("New cfl : ", value)
        print(self._model)

    @pyqtSlot(float)
    def change_x_0_value(self, value):
        self._model.x_0 = value
        print("Nex x_0 : ", value)
        print(self._model)

    @pyqtSlot(float)
    def change_t_value(self, value):
        self._model.T = value
        self.define_problem()
        print("Nex T : ", value)
        print(self._model)

    # Takes Signal from UI
    @pyqtSlot()
    def update_wl(self):
        self._model.rl = self._model_wl.r
        self._model.ul = self._model_wl.u
        self._model.pl = self._model_wl.p
        print(self._model)

    # Takes Signal from UI
    @pyqtSlot()
    def update_wr(self):
        self._model.rr = self._model_wr.r
        self._model.ur = self._model_wr.u
        self._model.pr = self._model_wr.p
        print(self._model)

    @property
    def model_wl(self):
        return self._model_wl

    @property
    def model_wr(self):
        return self._model_wr

    @property
    def model(self):
        return self._model

    # Takes Signal from UI
    @pyqtSlot(str)
    def change_type_solver(self, type_solver):
        self._model.type_solver = type_solver
        print(self._model.problem)

    # Takes Signal from UI
    @pyqtSlot(str)
    def change_problem(self, type_solver):
        self._model.problem = type_solver
        self._model.solve_problem()
        print(self._model.problem)

    @pyqtSlot()
    def define_problem(self):
        self._model.problem = self._model.type_solver
        self._model.solve_problem()
        print(self._model.problem)

    @pyqtSlot()
    def change_problem2(self):
        # self._model.problem = type_solver
        self.update_wl()
        self.update_wr()
        self._model.problem = self._model.type_solver
        self._model.solve_problem()
        print(self._model.problem)

    # @pyqtSlot(str)
    # def update_graphics(self, type_solver):
    #     self._model.problem = type_solver
    #     self._model.solve_problem()
    #     print(self._model.problem)
    #
