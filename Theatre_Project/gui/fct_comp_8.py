# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_8.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_8(object):
    def setupUi(self, fct_comp_8):
        fct_comp_8.setObjectName("fct_comp_8")
        fct_comp_8.resize(400, 300)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(fct_comp_8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(fct_comp_8)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(fct_comp_8)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_8)

    def retranslateUi(self, fct_comp_8):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_8.setWindowTitle(_translate("fct_comp_8", "Gestion de représentation"))
        self.label.setText(_translate("fct_comp_8", "TextLabel"))

