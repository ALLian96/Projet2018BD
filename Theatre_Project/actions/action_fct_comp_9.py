
import sqlite3
from utils import display
from utils import globalvar
from gui.fct_comp_9 import Ui_fct_comp_9
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

# Classe permettant d'afficher la fonction à compléter 9
class AppFctComp9(QDialog):
    ui = Ui_fct_comp_9()

    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui.setupUi(self)
        self.data = data
        self.refreshResult()
        self.refresh_noSpec()


    # Fonction de mise à jour de l'affichage
    def refreshResult(self):

        if not self.ui.lineEdit.text().strip():
            self.ui.table_fct_comp_9.setRowCount(0)
            display.refreshLabel(self.ui.label_bas, "Veuillez indiquer un login")
        else:
            try:
                cursor = self.data.cursor()
                result = cursor.execute(
                    "SELECT nom, prenom, noSpec, dateRep,noPlace,noRang FROM LesReservations NATURAL JOIN LesUsers WHERE login = ?",
                    [self.ui.lineEdit.text().strip()])
                display.refreshLabel(self.ui.label_bas, "")
            except Exception as e:
                self.ui.table_fct_comp_9.setRowCount(0)
                display.refreshLabel(self.ui.label_bas, "Impossible d'afficher les résultats : " + repr(e))
            else:
                i = display.refreshGenericData(self.ui.table_fct_comp_9, result)
                if i == 0:
                    display.refreshLabel(self.ui.label_bas, "Aucun résultat")
                self.refresh_s_noSpec()  #Losqu'il y a des donnée,  on peut les supprimer et on met à jour le contenu de box_ns_s

    # Partie add

    def refresh_noSpec(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT distinct noSpec FROM LesRepresentations_base")
        except Exception as e:
            self.ui.box_ns_a.clear()
        else:
            display.refreshGenericCombo(self.ui.box_ns_a, result)


    def refresh_dateRep(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT dateRep FROM LesRepresentations_base where noSpec = ?",
                                    [self.ui.box_ns_a.currentText().strip()])
        except Exception as e:
            self.ui.box_ns_a.clear()
        else:
            display.refreshGenericCombo(self.ui.box_dr_a, result)

    # Proposer numéro de place et numéro de place qui sont pas encore réservé
    def refresh_noRang(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("select distinct noRang from"
                                    "(select noRang,noPlace from LesPlaces "
                                    "except SELECT noRang,noPlace from LesPlaces natural join LesReservations "
                                    "where noSpec = ? and dateRep = ?)",
                                    [self.ui.box_ns_a.currentText().strip(), self.ui.box_dr_a.currentText().strip()])
        except Exception as e:
            self.ui.box_nr_a.clear()
        else:
            display.refreshGenericCombo(self.ui.box_nr_a, result)

    def refresh_noPlace(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "select noPlace from (select noPlace,noRang from LesPlaces except SELECT noPlace,noRang from LesPlaces natural join LesReservations order by noRang) where noRang = ?"
                , [self.ui.box_nr_a.currentText().strip()])
        except Exception as e:
            self.ui.box_nr_a.clear()
        else:
            display.refreshGenericCombo(self.ui.box_np_a, result)


    def add_reservation(self):
        if not self.ui.lineEdit.text().strip():
            self.ui.table_fct_comp_9.setRowCount(0)
            display.refreshLabel(self.ui.label_bas, "Veuillez indiquer un login pour ajouter")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("INSERT INTO LesReservations VALUES (?,?,?,?,?,?)",
                                    [self.ui.box_ns_a.currentText().strip(), self.ui.box_dr_a.currentText().strip(),
                                     self.ui.box_np_a.currentText().strip(), self.ui.box_nr_a.currentText().strip(),
                                     '06/01/2018 15:15:00', self.ui.lineEdit.text().strip()])

                #Comme on est en décembre 2018, c'est impossible d'ajouter une nouvelle valeur avec la date courante, donc ici on ajoute un date quelconque
            except Exception as e:
                self.ui.table_fct_comp_9.setRowCount(0)
                display.refreshLabel(self.ui.label_bas, "Impossible d'ajouter la réservation : " + repr(e))
            else:
                self.refreshResult()

    # Partie suppression


    def refresh_s_noSpec(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT distinct noSpec FROM LesReservations where login = ?",
                    [self.ui.lineEdit.text().strip()])
        except Exception as e:
            self.ui.box_ns_s.clear()
        else:
            display.refreshGenericCombo(self.ui.box_ns_s, result)

    def refresh_s_dateRep(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT dateRep FROM LesReservations where noSpec = ? and login = ?",
                                    [self.ui.box_ns_s.currentText().strip(), self.ui.lineEdit.text().strip()])
        except Exception as e:
            self.ui.box_ns_s.clear()
        else:
            display.refreshGenericCombo(self.ui.box_dr_s, result)

    def refresh_s_noRang(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute("SELECT distinct noRang FROM LesReservations where noSpec = ? and dateRep = ? and login = ? ",
                                    [self.ui.box_ns_s.currentText().strip(),
                                     self.ui.box_dr_s.currentText().strip(),
                                     self.ui.lineEdit.text().strip()])
        except Exception as e:
            self.ui.box_nr_s.clear()
        else:
            display.refreshGenericCombo(self.ui.box_nr_s, result)

    def refresh_s_noPlace(self):
        try:
            cursor = self.data.cursor()
            result = cursor.execute(
                "SELECT noPlace FROM LesReservations where noSpec = ? and dateRep = ? and noRang = ? and login = ? ",
                                    [self.ui.box_ns_s.currentText().strip(),
                                     self.ui.box_dr_s.currentText().strip(),
                                     self.ui.box_nr_s.currentText().strip(),
                                     self.ui.lineEdit.text().strip()])
        except Exception as e:
            self.ui.box_np_s.clear()
        else:
            display.refreshGenericCombo(self.ui.box_np_s, result)

    def delete_reservation(self):
        if not self.ui.lineEdit.text().strip():
            self.ui.table_fct_comp_9.setRowCount(0)
            display.refreshLabel(self.ui.label_bas, "Veuillez indiquer un login pour supprimer")
        else:
            try:
                cursor = self.data.cursor()
                cursor.execute("DELETE FROM LesReservations "
                               "where noSpec = ? and dateRep = ? and noPlace = ? and noRang = ? and login = ? ",
                                    [self.ui.box_ns_s.currentText().strip(),
                                     self.ui.box_dr_s.currentText().strip(),
                                     self.ui.box_np_s.currentText().strip(),
                                     self.ui.box_nr_s.currentText().strip(),
                                     self.ui.lineEdit.text().strip()])
            except Exception as e:
                self.ui.table_fct_comp_9.setRowCount(0)
                display.refreshLabel(self.ui.label_bas, "Impossible de supprimer la réservation : " + repr(e))
            else:
                self.refreshResult()
