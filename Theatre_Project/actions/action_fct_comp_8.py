

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
        self.refresh_noSpec()
        self.refresh_s_noSpec()

    # Fonction de mise à jour de l'affichage
    def refreshResult(self):
        display.refreshLabel(self.ui.label_mid, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "SELECT noSpec,dateRep,nbPlacesDispo FROM LesRepresentations")

        except Exception as e:
            self.ui.table_fct_8.setRowCount(0)
            display.refreshLabel(self.ui.label_mid, "Impossible d'afficher les résultats : " + repr(e))
        else:
            display.refreshGenericData(self.ui.table_fct_8, result)

    def refresh_noSpec(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT distinct noSpec FROM LesRepresentations_base")
        except Exception as e:
            self.ui.box_sp_a.clear()
        else:
            display.refreshGenericCombo(self.ui.box_sp_a, result)

    def add_representation(self):
        if not self.ui.lineEdit.text().strip():
            display.refreshLabel(self.ui.label_mid, "dateReprésentation ne doit pas être null.")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("INSERT INTO LesRepresentations_base VALUES (?,?)",
                            [self.ui.box_sp_a.currentText().strip(), self.ui.lineEdit.text().strip()])
            except Exception as e:
                self.ui.box_sp_a.clear()
                self.ui.lineEdit.clear()
                display.refreshLabel(self.ui.label_mid, "Impossible d'ajouter la représentation: " + repr(e))
            else:
                self.ui.lineEdit.clear()
                self.refreshResult()


    def refresh_s_noSpec(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT distinct noSpec FROM LesRepresentations_base")
        except Exception as e:
            self.ui.box_sp_s.clear()
        else:
            display.refreshGenericCombo(self.ui.box_sp_s, result)

    def refresh_s_dateRep(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT dateRep FROM LesRepresentations_base WHERE noSpec = ?",
                                    [self.ui.box_sp_s.currentText().strip()])
        except Exception as e:
            self.ui.box_dr_s.clear()
        else:
            display.refreshGenericCombo(self.ui.box_dr_s, result)

    def delete_representation(self):
        if not self.ui.box_sp_s.currentText().strip() or not self.ui.box_dr_s.currentText().strip():
            display.refreshLabel(self.ui.label_mid, "Choisir des éléments pour supprimer.")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("DELETE FROM LesRepresentations_base "
                               "where noSpec = ? and dateRep = ? ",
                               [self.ui.box_sp_s.currentText().strip(),
                                self.ui.box_dr_s.currentText().strip()])
            except Exception as e:
                self.ui.table_fct_8.setRowCount(0)
                display.refreshLabel(self.ui.label_mid, "Impossible de supprimer la représentation: " + repr(e))
            else:
                self.refreshResult()
