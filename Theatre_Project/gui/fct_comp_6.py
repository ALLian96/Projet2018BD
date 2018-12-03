# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_6.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_6(object):
    def setupUi(self, fct_comp_6):
        fct_comp_6.setObjectName("fct_comp_6")
        fct_comp_6.resize(637, 494)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_comp_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_fct_comp_6_1 = QtWidgets.QTableWidget(fct_comp_6)
        self.table_fct_comp_6_1.setObjectName("table_fct_comp_6_1")
        self.table_fct_comp_6_1.setColumnCount(3)
        self.table_fct_comp_6_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_6_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_6_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_6_1.setHorizontalHeaderItem(2, item)
        self.table_fct_comp_6_1.horizontalHeader().setDefaultSectionSize(200)
        self.table_fct_comp_6_1.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_6_1.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_6_1.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_6_1)
        self.table_fct_comp_6_2 = QtWidgets.QTableWidget(fct_comp_6)
        self.table_fct_comp_6_2.setObjectName("table_fct_comp_6_2")
        self.table_fct_comp_6_2.setColumnCount(2)
        self.table_fct_comp_6_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_6_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_6_2.setHorizontalHeaderItem(1, item)
        self.table_fct_comp_6_2.horizontalHeader().setDefaultSectionSize(200)
        self.table_fct_comp_6_2.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_6_2.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_6_2.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_6_2)
        self.label_fct_comp_6 = QtWidgets.QLabel(fct_comp_6)
        self.label_fct_comp_6.setText("")
        self.label_fct_comp_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_comp_6.setObjectName("label_fct_comp_6")
        self.verticalLayout.addWidget(self.label_fct_comp_6)

        self.retranslateUi(fct_comp_6)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_6)

    def retranslateUi(self, fct_comp_6):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_6.setWindowTitle(_translate("fct_comp_6", "Numéros des places libres"))
        item = self.table_fct_comp_6_1.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_6", "nomSpec"))
        item = self.table_fct_comp_6_1.horizontalHeaderItem(1)
        item.setText(_translate("fct_comp_6", "noSpec"))
        item = self.table_fct_comp_6_1.horizontalHeaderItem(2)
        item.setText(_translate("fct_comp_6", "dateRep"))
        item = self.table_fct_comp_6_2.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_6", "dateRep"))
        item = self.table_fct_comp_6_2.horizontalHeaderItem(1)
        item.setText(_translate("fct_comp_6", "noPlaceReserve"))

