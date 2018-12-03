
import sqlite3
from utils import display
from gui.fct_comp_5 import Ui_fct_comp_5
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot



class AppFctComp5(QDialog):

    ui = Ui_fct_comp_5()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_comp_P3_1, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "with X as (select noSpec,dateRep from LesRepresentations_base EXCEPT select noSpec,dateRep from LesTickets)"
                "select dateRep from X")
        except Exception as e:
            self.ui.table_fct_comp_P3_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_P3_1, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_comp_P3_1, result)