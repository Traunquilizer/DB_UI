# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchWin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWin(object):
    def setupUi(self, SearchWin):
        SearchWin.setObjectName("SearchWin")
        SearchWin.resize(1320, 510)
        self.line_search = QtWidgets.QLineEdit(SearchWin)
        self.line_search.setGeometry(QtCore.QRect(10, 5, 950, 22))
        self.line_search.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.line_search.setObjectName("line_search")
        self.comboBox_search_where = QtWidgets.QComboBox(SearchWin)
        self.comboBox_search_where.setGeometry(QtCore.QRect(965, 5, 170, 22))
        self.comboBox_search_where.setObjectName("comboBox_search_where")
        self.tableView_applications = QtWidgets.QTableView(SearchWin)
        self.tableView_applications.setGeometry(QtCore.QRect(5, 30, 1310, 480))
        self.tableView_applications.setAlternatingRowColors(True)
        self.tableView_applications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_applications.setWordWrap(True)
        self.tableView_applications.setObjectName("tableView_applications")
        self.tableView_applications.horizontalHeader().setDefaultSectionSize(110)
        self.tableView_applications.horizontalHeader().setMinimumSectionSize(30)
        self.tableView_applications.verticalHeader().setDefaultSectionSize(30)
        self.tableView_applications.verticalHeader().setMinimumSectionSize(29)
        self.add_button = QtWidgets.QPushButton(SearchWin)
        self.add_button.setGeometry(QtCore.QRect(1140, 5, 40, 22))
        self.add_button.setObjectName("add_button")

        self.retranslateUi(SearchWin)
        QtCore.QMetaObject.connectSlotsByName(SearchWin)

    def retranslateUi(self, SearchWin):
        _translate = QtCore.QCoreApplication.translate
        SearchWin.setWindowTitle(_translate("SearchWin", "Поиск по записям"))
        self.comboBox_search_where.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Сортировка по ...</p></body></html>"))
        self.add_button.setText(_translate("SearchWin", "+"))
