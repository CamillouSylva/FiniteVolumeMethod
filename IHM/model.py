#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Ce module sert de modèle aux vecteurs des variables primitives W_L = (r_l, u_l, p_l) et W_R = (r_r, u_r, p_r)
"""
from PyQt5.QtWidgets import QMessageBox, QStyledItemDelegate, QLineEdit
from PyQt5.QtCore import QModelIndex, Qt, QAbstractTableModel, QVariant

from FiniteVolumeMethod.Job.W import W


class ModelEditable(QAbstractTableModel):
    def __init__(self, data: W, table_header=None):
        """
        :param data: vecteur des variables primitives
        :param table_header: le header du tableau (QTableView()) qui doit être une liste de même que le vecteur W
        """
        QAbstractTableModel.__init__(self)
        if table_header is None:
            self.header = ["r", "u", "p"]
        else:
            self.header = table_header

        self._W = data

    def rowCount(self, parent=QModelIndex()):
        return 1

    def columnCount(self, parent=QModelIndex()):
        return len(self._W)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                if index.column() == 0:
                    value = self._W.r
                    return "%.4f" % value  # les valeurs sont arrondies à 4 chiffres après la virgule
                elif index.column() == 1:
                    value = self._W.u
                    return "%.4f" % value
                elif index.column() == 2:
                    value = self._W.p
                    return "%.4f" % value

            for column in range(0, self.columnCount()):
                if index.column() == column and role == Qt.TextAlignmentRole:
                    return Qt.AlignHCenter | Qt.AlignVCenter

            # if role == Qt.BackgroundRole and index.column() == 1:  # role == Qt.BackgroundRole --> pour colorier la
            #     # colonne et role == Qt.ForegroundRole pour les valeurs
            #     # See below for the profile structure.
            #     return QtGui.QColor("#ededed")  # (Qt.lightGray)

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # Si nous sommes dans l'orientation Horizontal (header horizontal), avec le rôle DisplayRole, nous renvoyons
        # le texte correspondant à la section (colonne).
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            # return self._data.columns[section]
            return self.header[section]
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        if role != Qt.EditRole:
            return False
        if index.row() < 0 or index.row() >= self.rowCount():
            return False
        if role == Qt.EditRole:
            try:
                if index.column() == 0:
                    self._W.r = float(value)
                elif index.column() == 1:
                    self._W.u = float(value)
                elif index.column() == 2:
                    self._W.p = float(value)
                self.dataChanged.emit(index, index)
            except ValueError:
                print('\n \n %%%%%%%%%%%% Valeur saisie invalide %%%%%%%%%%% \n \n ')
                self.message_box_critical(value)
            return True
        """le signal dataChanged() est envoyé à chaque fois que des éléments de données du modèle sont modifiés. Les
        changements des entêtes fournis par le modèle provoquent l'émission du signal headerDataChanged(). Si la
        structure des données sous-jacentes change, le modèle peut envoyer le signal layoutChanged() pour informer
        les vues qu'elles doivent réafficher les éléments présentés, en prenant la nouvelle structure en compte. """
        self.dataChanged.emit(index, index)
        self.layoutChanged.emit()
        # self.dataChanged.emit(index, index, (Qt.DisplayRole,))

        return False

    @staticmethod
    def message_box_critical(value):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Warning)
        msg.setText("{} : Valeur saisie incorrecte ".format(value))
        # msg.setInformativeText('Vérifiez que vous avez choisi un fichier .csv ')
        msg.setInformativeText("Seules les valeurs numériques sont autorisées.")
        msg.setWindowTitle("Warning ")
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setStyleSheet("QLabel{min-width:150 px; font-size: 13px;} QPushButton{ width:20px; font-size: 12px};"
                          "background-color: Ligthgray ; color : gray;font-size: 8pt; color: #888a80;")
        msg.exec_()

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        return self.createIndex(row, column, QModelIndex())

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        # if index.column() == 0:
        #     return Qt.ItemIsSelectable | Qt.ItemIsEnabled  # la colonne des abscisses n'est pas éditable
        # else:
        #     return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled

    @property
    def W(self):
        """
        return: Le vecteur contenant les valeurs primitives (r, u , p)
        """
        return self._W

    @property
    def r(self):
        """
        return: W.r
        """
        return self._W.r

    @property
    def u(self):
        """
        return: W.u
        """
        return self._W.u

    @property
    def p(self):
        """
        return: W.p
        """
        return self._W.p


class Delegate(QStyledItemDelegate):
    """
    Classe qui permet de personnaliser l'édition des éléments dans la 'vue' QTableView()
    """
    # Lorsque l'on souhaite uniquement personnaliser l'édition des éléments dans une vue et non le rendu,
    # on doit redéfinir quatre méthodes
    def __init__(self, parent=None, setModelDataEvent=None):
        super(Delegate, self).__init__(parent)
        self.setModelDataEvent = setModelDataEvent

    def createEditor(self, parent, option, index):
        """
        Args:
            parent:
            option:
            index:
        Returns: Le widget (éditeur) pour éditer l'item se trouvant à l'index index.
        """
        index.model().data(index, Qt.DisplayRole)
        return QLineEdit(parent)

    def setEditorData(self, editor, index):
        """
        Args:
            editor: l'éditeur
            index: l'index
        Returns: permet de transmettre à l'éditeur editor les données à afficher à partir du modèle se trouvant
                à l'index index.
        """
        value = index.model().data(index, Qt.DisplayRole)  # DisplayRole
        editor.setText(str(value))  # récupère la valeur de la cellule et applique la méthode définie dans setData
        print('Donnée éditée dans la case [{},{}] :'.format(index.row(), index.column()), value)

    def setModelData(self, editor, model, index):
        """
        Args:
            editor: l'éditeur
            model: le modèle
            index: l'index
        Returns: permet de récupérer les données de l'éditeur et de les stocker à l'intérieur du modèle, à l'index
                identifié par le paramètre index
        """
        model.setData(index, editor.text())
        # if self.setModelDataEvent is not None:
        if not self.setModelDataEvent is None:
            self.setModelDataEvent()
        row = index.row()
        col = index.column()
        # récup de la valeur modifiée
        valeur = index.model().data(index, Qt.DisplayRole)
        print("Case: [{},{}]   Nouvelle valeur: {} \n".format(row, col, valeur))

    def updateEditorGeometry(self, editor, option, index):
        """
        Args:
            editor: l'éditeur
            option:
            index: l'index
        Returns: Permet de redimensionner l'éditeur à la bonne taille lorsque la taille de la vue change
        """
        editor.setGeometry(option.rect)
