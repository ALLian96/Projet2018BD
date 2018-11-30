
import sqlite3
from utils import display
from gui.fct_comp_4 import Ui_fct_comp_4
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction à compléter 4
class AppFctComp4(QDialog):

    ui = Ui_fct_comp_4()

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshNoDos()

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):
        # TODO 4 : fonction à modifier pour que le numéro de dossier ne puisse être choisi que parmi ceux présents dans la base et que la catégorie ne propose que des valeurs possibles pour le dossier choisi, une fois le fichier ui correspondant mis à jour
        display.refreshLabel(self.ui.label_fct_comp_4, "")
        if not self.ui.comboBox_4_dos.currentText().strip():
            self.ui.table_fct_comp_4.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_4, "Veuillez indiquer un numéro de dossier")
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "SELECT * FROM LesTickets NATURAL JOIN LesPlaces NATURAL JOIN LesZones WHERE noDos = ? AND catZone=?",
                     [self.ui.comboBox_4_dos.currentText().strip(),self.ui.comboBox_4_categorie.currentText()])
            except Exception as e:
                self.ui.table_fct_comp_4.setRowCount(0)
                display.refreshLabel(self.ui.label_fct_comp_4, "Impossible d'afficher les résultats : " + repr(e))
            else:
                i = display.refreshGenericData(self.ui.table_fct_comp_4, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_fct_comp_4, "Aucun résultat")

    # Fonction de mise à jour des catégories
    def refreshCatList(self):
        display.refreshLabel(self.ui.label_fct_comp_4, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT DISTINCT catZone FROM LesDossiers NATURAL JOIN LesTickets NATURAL JOIN LesPlaces NATURAL JOIN LesZones WHERE noDos = ? ",
                                    [self.ui.comboBox_4_dos.currentText().strip()])
        except Exception as e:
            self.ui.comboBox_4_categorie.clear()
        else:
            i = display.refreshGenericCombo(self.ui.comboBox_4_categorie, result)

    # Fonction de sélection numéro des dossiers

    def refreshNoDos(self):

        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT noDos FROM LesDossiers")
        except Exception as e:
            self.ui.comboBox_4_dos.clear()
        else:
            display.refreshGenericCombo(self.ui.comboBox_4_dos, result)
