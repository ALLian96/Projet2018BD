# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_5(object):
    def setupUi(self, fct_comp_5):
        fct_comp_5.setObjectName("fct_comp_5")
        fct_comp_5.resize(457, 602)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_comp_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_fct_comp_P3_1 = QtWidgets.QTableWidget(fct_comp_5)
        self.table_fct_comp_P3_1.setObjectName("table_fct_comp_P3_1")
        self.table_fct_comp_P3_1.setColumnCount(1)
        self.table_fct_comp_P3_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_P3_1.setHorizontalHeaderItem(0, item)
        self.table_fct_comp_P3_1.horizontalHeader().setDefaultSectionSize(200)
        self.table_fct_comp_P3_1.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_P3_1.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_P3_1.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_P3_1)
        self.label_fct_comp_P3_1 = QtWidgets.QLabel(fct_comp_5)
        self.label_fct_comp_P3_1.setText("")
        self.label_fct_comp_P3_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_comp_P3_1.setObjectName("label_fct_comp_P3_1")
        self.verticalLayout.addWidget(self.label_fct_comp_P3_1)

        self.retranslateUi(fct_comp_5)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_5)

    def retranslateUi(self, fct_comp_5):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_5.setWindowTitle(_translate("fct_comp_5", "Numéros des places libres"))
        item = self.table_fct_comp_P3_1.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_5", "dateReprésentation"))

