# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchWinnew.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWin(object):
    def setupUi(self, SearchWin):
        SearchWin.setObjectName("SearchWin")
        SearchWin.resize(1200, 400)
        self.centralWidget = QtWidgets.QWidget(SearchWin)
        self.centralWidget.setObjectName("SearchWin")
        SearchWin.setCentralWidget(self.centralWidget)

        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_search = QtWidgets.QLineEdit(self.centralWidget)
        self.line_search.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.line_search.setObjectName("line_search")
        self.gridLayout.addWidget(self.line_search, 0, 0, 1, 1)
        self.comboBox_search_where = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_search_where.setObjectName("comboBox_search_where")
        self.gridLayout.addWidget(self.comboBox_search_where, 0, 1, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.centralWidget)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 0, 2, 1, 1)
        self.tableView_applications = QtWidgets.QTableView(self.centralWidget)
        self.tableView_applications.setAlternatingRowColors(True)
        self.tableView_applications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_applications.setWordWrap(True)
        self.tableView_applications.setObjectName("tableView_applications")
        self.tableView_applications.horizontalHeader().setDefaultSectionSize(110)
        self.tableView_applications.horizontalHeader().setMinimumSectionSize(30)
        self.tableView_applications.verticalHeader().setDefaultSectionSize(30)
        self.tableView_applications.verticalHeader().setMinimumSectionSize(29)
        self.gridLayout.addWidget(self.tableView_applications, 1, 0, 1, 3)

        self.retranslateUi(SearchWin)
        QtCore.QMetaObject.connectSlotsByName(SearchWin)

    def retranslateUi(self, SearchWin):
        _translate = QtCore.QCoreApplication.translate
        SearchWin.setWindowTitle(_translate("SearchWin", "Поиск по записям"))
        self.comboBox_search_where.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Сортировка по ...</p></body></html>"))
        self.add_button.setText(_translate("SearchWin", "+"))

