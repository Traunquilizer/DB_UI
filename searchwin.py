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
        SearchWin.resize(670, 400)
        self.search_button = QtWidgets.QPushButton(SearchWin)
        self.search_button.setGeometry(QtCore.QRect(440, 10, 111, 34))
        self.search_button.setObjectName("search_button")
        self.line_search = QtWidgets.QLineEdit(SearchWin)
        self.line_search.setGeometry(QtCore.QRect(10, 10, 241, 32))
        self.line_search.setObjectName("line_search")
        self.comboBox_search_by = QtWidgets.QComboBox(SearchWin)
        self.comboBox_search_by.setGeometry(QtCore.QRect(260, 10, 81, 32))
        self.comboBox_search_by.setObjectName("comboBox_search_by")
        self.comboBox_sort_by = QtWidgets.QComboBox(SearchWin)
        self.comboBox_sort_by.setGeometry(QtCore.QRect(350, 10, 83, 32))
        self.comboBox_sort_by.setObjectName("comboBox_sort_by")
        self.tableWidget_applications = QtWidgets.QTableWidget(SearchWin)
        self.tableWidget_applications.setGeometry(QtCore.QRect(0, 60, 631, 321))
        self.tableWidget_applications.setRowCount(2)
        self.tableWidget_applications.setObjectName("tableWidget_applications")
        self.tableWidget_applications.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_applications.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_applications.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_applications.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_applications.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_applications.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_applications.setHorizontalHeaderItem(5, item)

        self.retranslateUi(SearchWin)
        QtCore.QMetaObject.connectSlotsByName(SearchWin)

    def retranslateUi(self, SearchWin):
        _translate = QtCore.QCoreApplication.translate
        SearchWin.setWindowTitle(_translate("SearchWin", "Form"))
        self.search_button.setText(_translate("SearchWin", "Найти"))
        self.line_search.setText(_translate("SearchWin", "Поиск"))
        self.comboBox_search_by.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Поиск по ...</p></body></html>"))
        self.comboBox_sort_by.setWhatsThis(_translate("SearchWin", "<html><head/><body><p>Сортировка по ...</p></body></html>"))
        item = self.tableWidget_applications.horizontalHeaderItem(0)
        item.setText(_translate("SearchWin", "Дата"))
        item = self.tableWidget_applications.horizontalHeaderItem(1)
        item.setText(_translate("SearchWin", "Изделие"))
        item = self.tableWidget_applications.horizontalHeaderItem(2)
        item.setText(_translate("SearchWin", "ФИО"))
        item = self.tableWidget_applications.horizontalHeaderItem(3)
        item.setText(_translate("SearchWin", "Телефон"))
        item = self.tableWidget_applications.horizontalHeaderItem(4)
        item.setText(_translate("SearchWin", "Примечания"))
        item = self.tableWidget_applications.horizontalHeaderItem(5)
        item.setText(_translate("SearchWin", "Принял"))

