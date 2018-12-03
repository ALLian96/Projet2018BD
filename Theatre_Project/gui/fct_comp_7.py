# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fct_comp_7.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fct_comp_7(object):
    def setupUi(self, fct_comp_7):
        fct_comp_7.setObjectName("fct_comp_7")
        fct_comp_7.resize(457, 486)
        self.verticalLayout = QtWidgets.QVBoxLayout(fct_comp_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(fct_comp_7)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.table_fct_comp_7 = QtWidgets.QTableWidget(fct_comp_7)
        self.table_fct_comp_7.setObjectName("table_fct_comp_7")
        self.table_fct_comp_7.setColumnCount(3)
        self.table_fct_comp_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_fct_comp_7.setHorizontalHeaderItem(2, item)
        self.table_fct_comp_7.horizontalHeader().setDefaultSectionSize(200)
        self.table_fct_comp_7.horizontalHeader().setHighlightSections(True)
        self.table_fct_comp_7.horizontalHeader().setMinimumSectionSize(50)
        self.table_fct_comp_7.horizontalHeader().setStretchLastSection(True)
        self.table_fct_comp_7.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_fct_comp_7)
        self.label_fct_comp_7 = QtWidgets.QLabel(fct_comp_7)
        self.label_fct_comp_7.setText("")
        self.label_fct_comp_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fct_comp_7.setObjectName("label_fct_comp_7")
        self.verticalLayout.addWidget(self.label_fct_comp_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(fct_comp_7)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(fct_comp_7)
        self.pushButton.clicked.connect(fct_comp_7.close)
        QtCore.QMetaObject.connectSlotsByName(fct_comp_7)

    def retranslateUi(self, fct_comp_7):
        _translate = QtCore.QCoreApplication.translate
        fct_comp_7.setWindowTitle(_translate("fct_comp_7", "Affichier les représentations de  sepectacles"))
        self.label.setText(_translate("fct_comp_7", "Pour chaque spectacle, donner ses représentations et le nombre de places réservées(V2)"))
        item = self.table_fct_comp_7.horizontalHeaderItem(0)
        item.setText(_translate("fct_comp_7", "noSpec"))
        item = self.table_fct_comp_7.horizontalHeaderItem(1)
        item.setText(_translate("fct_comp_7", "dateRep"))
        item = self.table_fct_comp_7.horizontalHeaderItem(2)
        item.setText(_translate("fct_comp_7", "placeRéservée"))
        self.pushButton.setText(_translate("fct_comp_7", "Fermer"))

