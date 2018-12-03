

import sqlite3
from utils import display
from gui.fct_comp_8 import Ui_fct_comp_8
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
# Classe permettant d'afficher la fonction à compléter 8

class AppFctComp8(QDialog):
    ui = Ui_fct_comp_8()

    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label, "")

