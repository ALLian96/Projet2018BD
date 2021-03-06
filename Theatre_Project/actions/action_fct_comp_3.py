import sqlite3
from utils import display
from gui.fct_comp_3 import Ui_fct_comp_3
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction à compléter 3
class AppFctComp3(QDialog):

    ui = Ui_fct_comp_3()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data

        self.refreshCatList()

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):
        # TODO 3 : fonction à modifier pour remplacer la zone de saisie par une liste de valeurs issues de la BD une fois le fichier ui correspondant mis à jour
        display.refreshLabel(self.ui.label_fct_comp_3, "")
        if not self.ui.comboBox_fct_comp_3.currentText().strip():
            self.ui.table_fct_comp_3.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_3, "Veuillez indiquer un nom de catégorie")


        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "SELECT noPlace, noRang, noZone, prixZone FROM LesZones NATURAL JOIN LesPlaces WHERE catZone = ?",
                    [self.ui.comboBox_fct_comp_3.currentText().strip()])
            except Exception as e:
                self.ui.table_fct_comp_3.setRowCount(0)
                display.refreshLabel(self.ui.label_fct_comp_3, "Impossible d'afficher les résultats : " + repr(e))
            else:
                i = display.refreshGenericData(self.ui.table_fct_comp_3, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_fct_comp_3, "Aucun résultat")

    def refreshCatList(self):

            try:
                cursor = self.data.cursor()
                result = cursor.execute("SELECT catZone FROM LesZones")
            except Exception as e:
                self.ui.comboBox_fct_comp_3.clear()
            else:
                display.refreshGenericCombo(self.ui.comboBox_fct_comp_3, result)