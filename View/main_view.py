# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

from FiniteVolumeMethod.IHM.mainwindow_ui import Ui_MainWindow
from FiniteVolumeMethod.View import graphic_view as gr


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model

        self._main_controller = main_controller
        self._ui = Ui_MainWindow()

        self._ui.setupUi(self)
        self.setup_tableview()
        self.setup_connections()
        self.setup_model()
        self.enable_combobox_test()

    def setup_tableview(self):
        self.tableview_1 = self._ui.tableView_initial_states
        self.tableview_1.setModel(self._main_controller.model_wl)

        self.tableview_2 = self._ui.tableView_initial_states_2
        self.tableview_2.setModel(self._main_controller.model_wr)

        self.tableview_1.setItemDelegateForColumn(0, self._main_controller.delegate)
        self.tableview_1.setItemDelegateForColumn(1, self._main_controller.delegate)
        self.tableview_1.setItemDelegateForColumn(2, self._main_controller.delegate)
        self.tableview_2.setItemDelegateForColumn(0, self._main_controller.delegate)
        self.tableview_2.setItemDelegateForColumn(1, self._main_controller.delegate)
        self.tableview_2.setItemDelegateForColumn(2, self._main_controller.delegate)

    def setup_connections(self):
        # connect ui-widget to controller
        # if ui changes, it sends a signal to an slot on which we connect a controller class.
        # therefore we can receive the signal in the controller
        self._ui.spinBox_L.valueChanged.connect(self._main_controller.change_l_value)
        self._ui.spinBox_L.valueChanged.connect(self._main_controller.define_problem)

        self._ui.spinBox_Nx.valueChanged.connect(self._main_controller.change_nx_value)
        self._ui.spinBox_Nx.valueChanged.connect(self._main_controller.define_problem)

        self._ui.spinBox_cfl.valueChanged.connect(self._main_controller.change_cfl_value)
        self._ui.spinBox_cfl.valueChanged.connect(self._main_controller.define_problem)

        self._ui.spinBox_x0.valueChanged.connect(self._main_controller.change_x_0_value)
        self._ui.spinBox_x0.valueChanged.connect(self._main_controller.define_problem)

        self._ui.spinBox_T.valueChanged.connect(self._main_controller.change_t_value)
        #   self._ui.spinBox_T.valueChanged.connect(self._main_controller.define_problem)

        self._ui.comboBox_type_solver.currentTextChanged.connect(self._main_controller.change_type_solver)
        self._ui.comboBox_type_solver.currentTextChanged.connect(self._main_controller.change_problem)

        self._ui.comboBox_tests.currentIndexChanged.connect(self._main_controller.choose_test_case)
        self._ui.comboBox_tests.currentIndexChanged.connect(self._main_controller.define_problem)

        self._ui.checkBox.stateChanged.connect(self.enable_combobox_test)

        self._ui.btn_run.clicked.connect(self.plot)

    def setup_model(self):
        # listen for model event signals
        # connect the method to update the ui to the slots of the model
        # if model sends/emits a signal the ui gets notified
        self._model.L_changed[float].connect(self.on_l_changed)
        self._model.str_value_changed[str].connect(self.on_name_changed)

        self._main_controller.model_wl.dataChanged.connect(self._main_controller.update_wl)
        self._main_controller.model_wr.dataChanged.connect(self._main_controller.update_wr)

        # self._model.float_value_changed[float].connect(self._main_controller.change_problem)
        self._main_controller.model_wl.dataChanged.connect(self._main_controller.change_problem2)
        self._main_controller.model_wr.dataChanged.connect(self._main_controller.change_problem2)

        self._main_controller.change_type_solver(self._ui.comboBox_type_solver.currentText())
        self._main_controller.change_problem(
            self._ui.comboBox_type_solver.currentText())  # on définit le problème en fonction de la combobox

    # self._model.problem_changed[str].connect(self._main_controller.change_problem)

    # self._model.update_wr.connect(self._main_controller.change_problem)

    # def tableview_updated(self):
    #     self._main_controller.model_wl.dataChaged

    def enable_combobox_test(self):
        """
        :return: Méthode appelée lorsqu'on coche ou décoche la QCheckbox.
        Elle désactive et active les QSpinBox (QDoubleSpinBox) et les
        QTableView selon l'état de la QCheckBox.
        """
        if self._ui.checkBox.isChecked():
            self._ui.comboBox_tests.setEnabled(True)
            self._ui.spinBox_L.setEnabled(False)
            self._ui.spinBox_Nx.setEnabled(False)
            self._ui.spinBox_x0.setEnabled(False)
            self._ui.spinBox_T.setEnabled(False)
            self._ui.spinBox_cfl.setEnabled(False)
            self._ui.tableView_initial_states.setEnabled(False)
            self._ui.tableView_initial_states_2.setEnabled(False)

        else:
            self._ui.comboBox_tests.setEnabled(False)
            self._ui.spinBox_L.setEnabled(True)
            self._ui.spinBox_Nx.setEnabled(True)
            self._ui.spinBox_x0.setEnabled(True)
            self._ui.spinBox_T.setEnabled(True)
            self._ui.spinBox_cfl.setEnabled(True)
            self._ui.tableView_initial_states.setEnabled(True)
            self._ui.tableView_initial_states_2.setEnabled(True)
            self._main_controller.change_problem2()

    @pyqtSlot(float)
    def on_l_changed(self, value):
        self._ui.spinBox_L.setValue(value)
        print("change_l_value vue : ", value)

    @pyqtSlot(str)
    def on_name_changed(self, value):
        # self._ui.spinBox_L.setValue(value)
        print("name changed : ", value)

    def plot_1(self):
        graph = gr.Graphic(self._ui.mycanvas_1,
                           self._model.xm, self._model.r,
                           x_label="Position $x_m$", y_label="Densité \u03C1")
        graph.plot()

    def plot_2(self):
        graph2 = gr.Graphic(self._ui.mycanvas_2,
                            self._model.xm, self._model.u,
                            x_label="Position $x_m$", y_label="Vitesse $u$")
        graph2.plot()

    def plot_3(self):
        graph3 = gr.Graphic(self._ui.mycanvas_3,
                            self._model.xm, self._model.e,
                            x_label="Position $x_m$", y_label="Énergie interne $e$")
        graph3.plot()

    def plot_4(self):
        graph4 = gr.Graphic(self._ui.mycanvas_4,
                            self._model.xm, self._model.p,
                            x_label="Position $x_m$", y_label="Pression $p$")
        graph4.plot()

    def plot(self):
        #    self._main_controller.define_problem()
        self.plot_1()
        self.plot_2()
        self.plot_3()
        self.plot_4()
