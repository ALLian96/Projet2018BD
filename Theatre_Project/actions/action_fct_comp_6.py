
import sqlite3
from utils import display
from gui.fct_comp_6 import Ui_fct_comp_6
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot


class AppFctComp6(QDialog):

    ui = Ui_fct_comp_6()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()
        self.refreshResult2()


    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        display.refreshLabel(self.ui.label_fct_comp_6, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "SELECT nomSpec,noSpec,dateRep from LesRepresentations_base natural join LesSpectacles")
        except Exception as e:
            self.ui.table_fct_comp_6_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_6, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_comp_6_1, result)

    @pyqtSlot()
    def refreshResult2(self):
        display.refreshLabel(self.ui.label_fct_comp_6, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "select LRb.dateRep,count(noPlace) as Noplace from LesRepresentations_base LRb LEFT OUTER JOIN LesTickets LT on LRb.noSpec = LT.noSpec and LRb.dateRep = LT.dateRep"
                " group by  LRb.dateRep")
        except Exception as e:
            self.ui.table_fct_comp_6_2.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_6, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_comp_6_2, result)