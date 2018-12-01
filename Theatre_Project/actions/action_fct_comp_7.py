
import sqlite3
from utils import display
from gui.fct_comp_7 import Ui_fct_comp_7
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction à compléter 7
class AppFctComp7(QDialog):
    ui = Ui_fct_comp_7()

    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):

        display.refreshLabel(self.ui.label_fct_comp_7, "")
        try:
            cursor = self.data.cursor()
            # DONE 1 : mettre à jour la requête et changer aussi le fichier ui correspondant
            result = cursor.execute("select LRb.noSpec,LRb.dateRep,count(noPlace) as placeReserve from LesRepresentations_base LRb left outer join LesTickets LT on LRb.noSpec = LT.noSpec and LRb.dateRep = LT.dateRep GROUP BY LRb.noSpec,LRb.dateRep")
            display.refreshGenericData(self.ui.table_fct_comp_7, result)
        except Exception as e:
            self.ui.table_fct_comp_7.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_7, "Impossible d'afficher les résultats : " + repr(e))
