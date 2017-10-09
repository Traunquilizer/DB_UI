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
        SearchWin.resize(1361, 520)
        self.search_button = QtWidgets.QPushButton(SearchWin)
        self.search_button.setGeometry(QtCore.QRect(880, 10, 81, 30))
        self.search_button.setObjectName("search_button")
        self.line_search = QtWidgets.QLineEdit(SearchWin)
        self.line_search.setGeometry(QtCore.QRect(10, 10, 553, 30))
        self.line_search.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.line_search.setObjectName("line_search")
        self.comboBox_search_where = QtWidgets.QComboBox(SearchWin)
        self.comboBox_search_where.setGeometry(QtCore.QRect(700, 10, 171, 30))
        self.comboBox_search_where.setObjectName("comboBox_search_where")
        self.comboBox_search_where.addItem("")
        self.comboBox_search_where.addItem("")
        self.comboBox_search_where.addItem("")
        self.comboBox_search_where.addItem("")
        self.comboBox_search_where.addItem("")
        self.comboBox_search_where.addItem("")
        self.tableView_applications = QtWidgets.QTableView(SearchWin)
        self.tableView_applications.setGeometry(QtCore.QRect(10, 50, 1341, 461))
        self.tableView_applications.setAlternatingRowColors(True)
        self.tableView_applications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView_applications.setWordWrap(True)
        self.tableView_applications.setObjectName("tableView_applications")
        self.tableView_applications.horizontalHeader().setDefaultSectionSize(110)
        self.tableView_applications.horizontalHeader().setMinimumSectionSize(30)
        self.tableView_applications.verticalHeader().setDefaultSectionSize(30)
        self.tableView_applications.verticalHeader().setMinimumSectionSize(29)
        self.add_button = QtWidgets.QPushButton(SearchWin)
        self.add_button.setGeometry(QtCore.QRect(1118, 10, 116, 30))
        self.add_button.setObjectName("add_button")
        self.comboBox_sort = QtWidgets.QComboBox(SearchWin)
        self.comboBox_sort.setGeometry(QtCore.QRect(564, 10, 131, 30))
        self.comboBox_sort.setObjectName("comboBox_sort")
        self.comboBox_sort.addItem("")
        self.comboBox_sort.addItem("")
        self.delete_button = QtWidgets.QPushButton(SearchWin)
        self.delete_button.setGeometry(QtCore.QRect(1235, 10, 116, 30))
        self.delete_button.setObjectName("delete_button")

        self.retranslateUi(SearchWin)
        QtCore.QMetaObject.connectSlotsByName(SearchWin)

    def retranslateUi(self, SearchWin):
        _translate = QtCore.QCoreApplication.translate
        SearchWin.setWindowTitle(_translate("SearchWin", "Поиск по записям"))
        self.search_button.setText(_translate("SearchWin", "Найти"))
        self.comboBox_search_where.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Сортировка по ...</p></body></html>"))
        self.comboBox_search_where.setItemText(0, _translate("SearchWin", "Заявки"))
        self.comboBox_search_where.setItemText(1, _translate("SearchWin", "Клиенты"))
        self.comboBox_search_where.setItemText(2, _translate("SearchWin", "Приёмщики склада"))
        self.comboBox_search_where.setItemText(3, _translate("SearchWin", "Работники"))
        self.comboBox_search_where.setItemText(4, _translate("SearchWin", "Операции"))
        self.comboBox_search_where.setItemText(5, _translate("SearchWin", "Изделия"))
        self.add_button.setText(_translate("SearchWin", "Добавить"))
        self.comboBox_sort.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Поиск по ...</p></body></html>"))
        self.comboBox_sort.setItemText(0, _translate("SearchWin", "Сначала новые"))
        self.comboBox_sort.setItemText(1, _translate("SearchWin", "Сначала старые"))
        self.delete_button.setText(_translate("SearchWin", "Удалить"))

