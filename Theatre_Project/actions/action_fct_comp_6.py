
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

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_comp_P3_2, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "with X as (  select nomSpec, noSpec  from LesTickets natural join lesSpectacles) select nomSpec, dateRep, count(noSpec) as nbPlaceRes from X natural join LesSpectacles natural join LesRepresentations group by nomSpec, dateRep")
        except Exception as e:
            self.ui.table_fct_comp_P3_2.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_P3_2, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_comp_P3_2, result)