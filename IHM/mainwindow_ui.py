# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtCore, QtGui, QtWidgets

from FiniteVolumeMethod.IHM.canvas_matplotlib import CanvasMatplotlib

file_path = os.path.abspath(os.path.dirname(__file__))
icon_path = f"{os.path.dirname(file_path)}/resources/"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1200, 900)
        # Get current screen geometry
        self.Screen = QtWidgets.QDesktopWidget().screenGeometry()
        print(self.Screen, self.Screen.height(), self.Screen.width())
        MainWindow.resize(self.Screen.width(), self.Screen.height())
        # MainWindow.showMaximized()  # Ne marche pas sous Windows
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_L = QtWidgets.QHBoxLayout()
        self.horizontalLayout_L.setObjectName("horizontalLayout_L")

        self.horizontalLayout_cfl = QtWidgets.QHBoxLayout()
        self.horizontalLayout_cfl.setObjectName("horizontalLayout_cfl")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_domain_length = QtWidgets.QLabel(self.layoutWidget)
        self.label_domain_length.setObjectName("label_domain_length")
        self.horizontalLayout_L.addWidget(self.label_domain_length)
        locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom)
        self.spinBox_L = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spinBox_L.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_L.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spinBox_L.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBox_L.setPrefix("")
        self.spinBox_L.setMinimum(0.1)
        self.spinBox_L.setMaximum(1000)
        # self.spinBox_L.setSingleStep(1)
        self.spinBox_L.setProperty("value", 1)
        self.spinBox_L.setSingleStep(0.01)
        self.spinBox_L.setDecimals(2)
        self.spinBox_L.setLocale(locale)
        # self.spinBox_L.setDisplayIntegerBase(10)
        self.spinBox_L.setObjectName("spinBox_L")
        self.horizontalLayout_L.addWidget(self.spinBox_L)
        spacerItem_L = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_L.addItem(spacerItem_L)
        #  self.verticalLayout_2.addWidget(self.label_domain_length)
        self.verticalLayout_2.addLayout(self.horizontalLayout_L)

        self.label_number_cells = QtWidgets.QLabel(self.layoutWidget)
        self.label_number_cells.setObjectName("label_number_cells")
        self.horizontalLayout_2.addWidget(self.label_number_cells)

        self.spinBox_Nx = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_Nx.setObjectName("spinBox_Nx")
        self.spinBox_Nx.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_Nx.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spinBox_Nx.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBox_Nx.setPrefix("")
        self.spinBox_Nx.setMinimum(1)
        self.spinBox_Nx.setMaximum(1000)
        self.spinBox_Nx.setSingleStep(1)
        self.spinBox_Nx.setProperty("value", 100)
        self.spinBox_Nx.setDisplayIntegerBase(10)
        self.spinBox_Nx.setLocale(locale)

        self.horizontalLayout_2.addWidget(self.spinBox_Nx)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_cfl_condition = QtWidgets.QLabel(self.layoutWidget)
        self.label_cfl_condition.setObjectName("label_cfl_condition")
        self.horizontalLayout_cfl.addWidget(self.label_cfl_condition)

        self.spinBox_cfl = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spinBox_cfl.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_cfl.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spinBox_cfl.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBox_cfl.setPrefix("")
        self.spinBox_cfl.setMinimum(0.05)
        self.spinBox_cfl.setMaximum(1)
        # self.spinBox_cfl.setSingleStep(1)
        self.spinBox_cfl.setProperty("value", 0.9)
        self.spinBox_cfl.setSingleStep(0.01)
        self.spinBox_cfl.setDecimals(2)
        self.spinBox_cfl.setLocale(locale)

        # self.spinBox_cfl.setDisplayIntegerBase(2)
        self.spinBox_cfl.setObjectName("spinBox_cfl")
        self.horizontalLayout_cfl.addWidget(self.spinBox_cfl)
        spacerItem_cfl = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_cfl.addItem(spacerItem_cfl)
        #  self.verticalLayout_2.addWidget(self.label_domain_length)
        self.verticalLayout_2.addLayout(self.horizontalLayout_cfl)

        self.horizontalLayout_x0 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_x0.setObjectName("horizontalLayout_x0")

        self.label_x0_condition = QtWidgets.QLabel(self.layoutWidget)
        self.label_x0_condition.setObjectName("label_x0_condition")
        self.horizontalLayout_x0.addWidget(self.label_x0_condition)

        self.spinBox_x0 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spinBox_x0.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_x0.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spinBox_x0.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBox_x0.setPrefix("")
        self.spinBox_x0.setMinimum(-9999)
        self.spinBox_x0.setMaximum(9999)
        # self.spinBox_x0.setSingleStep(1)
        self.spinBox_x0.setProperty("value", 0.3)
        self.spinBox_x0.setSingleStep(0.01)
        self.spinBox_x0.setDecimals(2)
        self.spinBox_x0.setLocale(locale)

        # self.spinBox_x0.setDisplayIntegerBase(2)
        self.spinBox_x0.setObjectName("spinBox_x0")
        self.horizontalLayout_x0.addWidget(self.spinBox_x0)
        spacerItem_x0 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_x0.addItem(spacerItem_x0)
        #  self.verticalLayout_2.addWidget(self.label_domain_length)
        self.verticalLayout_2.addLayout(self.horizontalLayout_x0)

        self.horizontalLayout_T = QtWidgets.QHBoxLayout()
        self.horizontalLayout_T.setObjectName("horizontalLayout_cfl")

        self.label_T_condition = QtWidgets.QLabel(self.layoutWidget)
        self.label_T_condition.setObjectName("label_T_condition")
        self.horizontalLayout_T.addWidget(self.label_T_condition)

        self.spinBox_T = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.spinBox_T.setObjectName("spinBox_T")
        self.spinBox_T.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_T.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spinBox_T.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.spinBox_T.setPrefix("")
        self.spinBox_T.setMinimum(0.01)
        self.spinBox_T.setMaximum(999)
        # self.spinBox_T0.setSingleStep(1)
        self.spinBox_T.setProperty("value", 0.2)
        self.spinBox_T.setSingleStep(0.01)
        self.spinBox_T.setDecimals(2)
        self.spinBox_T.setLocale(locale)

        # self.spinBox_T.setDisplayIntegerBase(2)
        self.horizontalLayout_T.addWidget(self.spinBox_T)
        spacerItem_T = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_T.addItem(spacerItem_T)
        #  self.verticalLayout_2.addWidget(self.label_domain_length)
        self.verticalLayout_2.addLayout(self.horizontalLayout_T)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_initial_states = QtWidgets.QLabel(self.layoutWidget)
        self.label_initial_states.setObjectName("label_initial_states")
        self.verticalLayout.addWidget(self.label_initial_states)

        self.tableView_initial_states = QtWidgets.QTableView(self.layoutWidget)
        self.tableView_initial_states.horizontalHeader().setStretchLastSection(True)


        self.tableView_initial_states.setObjectName("tableView_initial_states")
        self.verticalLayout.addWidget(self.tableView_initial_states)

        self.label_initial_states_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_initial_states_2.setObjectName("label_initial_states_2")
        self.verticalLayout.addWidget(self.label_initial_states_2)

        self.tableView_initial_states_2 = QtWidgets.QTableView(self.layoutWidget)
        self.tableView_initial_states_2.setObjectName("tableView_initial_states_2")
        self.tableView_initial_states_2.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableView_initial_states_2)

        self.label_initial_states_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_initial_states_3.setObjectName("label_initial_states_3")
        self.verticalLayout.addWidget(self.label_initial_states_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_type_solvers = QtWidgets.QLabel(self.layoutWidget)
        self.label_type_solvers.setObjectName("label_type_solvers")
        self.horizontalLayout.addWidget(self.label_type_solvers)
        self.comboBox_type_solver = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_type_solver.setMinimumSize(QtCore.QSize(81, 31))
        self.comboBox_type_solver.setObjectName("comboBox_type_solver")
        self.comboBox_type_solver.addItem("")
        self.comboBox_type_solver.addItem("")
        self.comboBox_type_solver.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_type_solver)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox_tests = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_tests.setMinimumSize(QtCore.QSize(101, 31))
        self.comboBox_tests.setObjectName("comboBox_tests")
        self.comboBox_tests.addItem("")
        self.comboBox_tests.addItem("")
        self.comboBox_tests.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_tests)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_btn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btn.setObjectName("horizontalLayout_btn")
        self.btn_run = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_run.setMaximumSize(QtCore.QSize(60, 60))
        btn_size = QSize(50, 60)

        icon_btn = QIcon()
        icon_btn.addPixmap(
            QPixmap(f"{icon_path}go_right.png"))
        self.btn_run.setIcon(icon_btn)
        self.btn_run.setIconSize(btn_size)
        self.horizontalLayout_btn.addWidget(self.btn_run)
        self.verticalLayout_2.addLayout(self.horizontalLayout_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_canvas_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_canvas_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_canvas_1.setObjectName("verticalLayout_canvas_1")

        self.mycanvas_1 = CanvasMatplotlib(width=4, height=5,
                                           dpi=100)

        self.toolbar_1 = NavigationToolbar(self.mycanvas_1, self.verticalLayoutWidget)
        self.verticalLayout_canvas_1.addWidget(self.toolbar_1)
        self.verticalLayout_canvas_1.addWidget(self.mycanvas_1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_canvas_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_canvas_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_canvas_2.setObjectName("verticalLayout_canvas_2")

        self.mycanvas_2 = CanvasMatplotlib(width=4, height=5,
                                           dpi=100)

        self.toolbar_2 = NavigationToolbar(self.mycanvas_2, self.verticalLayoutWidget_2)
        self.verticalLayout_canvas_2.addWidget(self.toolbar_2)
        self.verticalLayout_canvas_2.addWidget(self.mycanvas_2)

        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_2)
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.splitter_4)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_canvas_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_canvas_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_canvas_4.setObjectName("verticalLayout_canvas_4")

        self.mycanvas_4 = CanvasMatplotlib(width=4, height=5,
                                           dpi=100)

        self.toolbar_4 = NavigationToolbar(self.mycanvas_4, self.verticalLayoutWidget_4)
        self.verticalLayout_canvas_4.addWidget(self.toolbar_4)
        self.verticalLayout_canvas_4.addWidget(self.mycanvas_4)

        #
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter_4)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_canvas_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_canvas_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_canvas_3.setObjectName("verticalLayout_canvas_3")

        self.mycanvas_3 = CanvasMatplotlib(width=4, height=5,
                                           dpi=100)

        self.toolbar_3 = NavigationToolbar(self.mycanvas_3, self.verticalLayoutWidget_3)
        self.verticalLayout_canvas_3.addWidget(self.toolbar_3)
        self.verticalLayout_canvas_3.addWidget(self.mycanvas_3)

        self.horizontalLayout_4.addWidget(self.splitter_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solveurs de Riemann approchés (Rusanov, HLL et HLLC) "))
        self.label_domain_length.setText(_translate("MainWindow",
                                                    "<html><head/><body><p><span style=\" color:#0000ff;\">Longueur "
                                                    "du domaine :</span></p></body></html>"))
        self.label_number_cells.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" color:#0000ff;\">Nombre de "
                                                   "mailles :</span></p></body></html>"))
        self.label_cfl_condition.setText(_translate("MainWindow",
                                                    "<html><head/><body><p><span style=\" color:#0000ff;\">Condition "
                                                    "CFL :</span></p></body></html>"))

        self.label_x0_condition.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" color:#0000ff;\">Point de "
                                                   "discontinuité x_0 :</span></p></body></html>"))
        self.label_T_condition.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" color:#0000ff;\">Temps "
                                                  "final T :</span></p></body></html>"))

        self.label_initial_states.setText(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" "
                                                     "color:#0000ff;\">Définition des états initiaux à "
                                                     "gauche</span></p></body></html>"))
        self.label_initial_states_2.setText(_translate("MainWindow",
                                                       "<html><head/><body><p><span style=\" "
                                                       "color:#0000ff;\">Définition des états initiaux à "
                                                       "droite</span></p></body></html>"))
        # self.label_initial_states_3.setText(_translate("MainWindow",
        #                                                "<html><head/><body><p><span style=\" "
        #                                                "color:#0000ff;\">Définition du temps final et le point de "
        #                                                "discontinuité </span></p></body></html>"))
        self.label_type_solvers.setText(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" color:#0000ff;\">Type de "
                                                   "solveur : </span></p></body></html>"))
        self.comboBox_tests.setToolTip(_translate("MainWindow", "Cas test 1 :\n\tr_l = 1.0, u_l =0.0, p_l=1.0\n\tr_r = "
                                                                "0.125, u_r =0.0, p_r=0.1\n\tL= 1.0, T= 0.2, x_0 = "
                                                                "0.3, CFL =0.9\n"
                                                                "Cas test 2 :\n\tr_l = 1.0, u_l =-2.0, p_l=0.4\n\tr_r "
                                                                "= "
                                                                "1.0, u_r =2.0, p_r=0.4\n\tL= 1.0, T= 0.15, x_0 = "
                                                                "0.5, CFL =0.9\n"
                                                                "Cas test 3 :\n\tr_l = 1.0, u_l =0.0, "
                                                                "p_l=1000.0\n\tr_r = "
                                                                "1.0, u_r =0.0, p_r=0.01\n\tL= 1.0, T= 0.012, x_0 = "
                                                                "0.5, CFL =0.9"

                                                  ))
        self.comboBox_type_solver.setItemText(0, _translate("MainWindow", "Rusanov"))
        self.comboBox_type_solver.setItemText(1, _translate("MainWindow", "HLL"))
        self.comboBox_type_solver.setItemText(2, _translate("MainWindow", "HLLC"))
        self.checkBox.setText(_translate("MainWindow", "Utiliser les tests prédifinis"))
        self.comboBox_tests.setItemText(0, _translate("MainWindow", "Cas test 1"))
        self.comboBox_tests.setItemText(1, _translate("MainWindow", "Cas test 2"))
        self.comboBox_tests.setItemText(2, _translate("MainWindow", "Cas test 3"))
        self.btn_run.setToolTip(_translate("MainWindow", "Lancer le solveur"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
