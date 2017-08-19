# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchWin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWin(object):
    def setupUi(self, SearchWin):
        SearchWin.setObjectName("SearchWin")
        SearchWin.resize(843, 400)
        self.search_button = QtWidgets.QPushButton(SearchWin)
        self.search_button.setGeometry(QtCore.QRect(710, 10, 111, 34))
        self.search_button.setObjectName("search_button")
        self.line_search = QtWidgets.QLineEdit(SearchWin)
        self.line_search.setGeometry(QtCore.QRect(10, 10, 401, 32))
        self.line_search.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.line_search.setObjectName("line_search")
        self.comboBox_search_by = QtWidgets.QComboBox(SearchWin)
        self.comboBox_search_by.setGeometry(QtCore.QRect(440, 10, 121, 32))
        self.comboBox_search_by.setObjectName("comboBox_search_by")
        self.comboBox_sort_by = QtWidgets.QComboBox(SearchWin)
        self.comboBox_sort_by.setGeometry(QtCore.QRect(570, 10, 131, 32))
        self.comboBox_sort_by.setObjectName("comboBox_sort_by")
        self.tableView_applications = QtWidgets.QTableView(SearchWin)
        self.tableView_applications.setGeometry(QtCore.QRect(0, 60, 831, 321))
        self.tableView_applications.setAlternatingRowColors(True)
        self.tableView_applications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_applications.setWordWrap(False)
        self.tableView_applications.setObjectName("tableView_applications")
        self.tableView_applications.horizontalHeader().setDefaultSectionSize(110)
        self.tableView_applications.horizontalHeader().setMinimumSectionSize(30)
        self.tableView_applications.verticalHeader().setDefaultSectionSize(30)
        self.tableView_applications.verticalHeader().setMinimumSectionSize(29)

        self.retranslateUi(SearchWin)
        QtCore.QMetaObject.connectSlotsByName(SearchWin)

    def retranslateUi(self, SearchWin):
        _translate = QtCore.QCoreApplication.translate
        SearchWin.setWindowTitle(_translate("SearchWin", "Поиск по принятым заявкам"))
        self.search_button.setText(_translate("SearchWin", "Найти"))
        self.comboBox_search_by.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Поиск по ...</p></body></html>"))
        self.comboBox_sort_by.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Сортировка по ...</p></body></html>"))

