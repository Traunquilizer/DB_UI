# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inserting_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets

client = pymongo.MongoClient()
db = client.Architecht

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 328)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        # self.lab_start_phone = QtWidgets.QLabel(self.centralWidget)
        # self.lab_start_phone.setGeometry(QtCore.QRect(20, 170, 21, 21))
        # self.lab_start_phone.setObjectName("lab_start_phone")
        self.dateEdit = QtWidgets.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(20, 220, 110, 21))
        self.dateEdit.setAutoFillBackground(False)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.lab_stuff = QtWidgets.QLabel(self.centralWidget)
        self.lab_stuff.setGeometry(QtCore.QRect(290, 100, 131, 21))
        self.lab_stuff.setObjectName("lab_stuff")
        self.lab_phone = QtWidgets.QLabel(self.centralWidget)
        self.lab_phone.setGeometry(QtCore.QRect(20, 150, 131, 21))
        self.lab_phone.setObjectName("lab_phone")
        self.lab_product_name = QtWidgets.QLabel(self.centralWidget)
        self.lab_product_name.setGeometry(QtCore.QRect(20, 50, 131, 21))
        self.lab_product_name.setObjectName("lab_product_name")
        self.lab_date = QtWidgets.QLabel(self.centralWidget)
        self.lab_date.setGeometry(QtCore.QRect(20, 200, 131, 21))
        self.lab_date.setObjectName("lab_date")
        self.button_proceed = QtWidgets.QPushButton(self.centralWidget)
        self.button_proceed.setGeometry(QtCore.QRect(290, 270, 261, 21))
        self.button_proceed.setObjectName("button_proceed")
        self.textf_stuff = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.textf_stuff.setGeometry(QtCore.QRect(290, 120, 261, 121))
        self.textf_stuff.setObjectName("textf_stuff")
        self.lab_receiver = QtWidgets.QLabel(self.centralWidget)
        self.lab_receiver.setGeometry(QtCore.QRect(20, 250, 131, 21))
        self.lab_receiver.setObjectName("lab_receiver")
        self.button_search = QtWidgets.QPushButton(self.centralWidget)
        self.button_search.setGeometry(QtCore.QRect(20, 20, 211, 21))
        self.button_search.setObjectName("button_search")
        self.lab_name = QtWidgets.QLabel(self.centralWidget)
        self.lab_name.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.lab_name.setObjectName("lab_name")
        self.cBox_receiver = QtWidgets.QComboBox(self.centralWidget)
        self.cBox_receiver.setGeometry(QtCore.QRect(20, 270, 121, 21))
        self.cBox_receiver.setMaxVisibleItems(4)
        self.cBox_receiver.setObjectName("cBox_receiver")
        for i in list(enumerate(db.Receivers.find())):
            self.cBox_receiver.addItem("")
        self.line_product_name = QtWidgets.QLineEdit(self.centralWidget)
        self.line_product_name.setGeometry(QtCore.QRect(20, 70, 251, 21))
        self.line_product_name.setObjectName("line_product_name")
        self.line_name = QtWidgets.QLineEdit(self.centralWidget)
        self.line_name.setGeometry(QtCore.QRect(20, 120, 251, 21))
        self.line_name.setObjectName("line_name")
        self.line_phone = QtWidgets.QLineEdit(self.centralWidget)
        self.line_phone.setGeometry(QtCore.QRect(20, 170, 251, 21))
        self.line_phone.setObjectName("line_phone")
        self.checkBox_guarantee = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_guarantee.setGeometry(QtCore.QRect(290, 70, 131, 22))
        self.checkBox_guarantee.setObjectName("checkBox_guarantee")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.line_product_name, self.checkBox_guarantee)
        MainWindow.setTabOrder(self.checkBox_guarantee, self.line_name)
        MainWindow.setTabOrder(self.line_name, self.line_phone)
        MainWindow.setTabOrder(self.line_phone, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.cBox_receiver)
        MainWindow.setTabOrder(self.cBox_receiver, self.button_proceed)
        MainWindow.setTabOrder(self.button_proceed, self.button_search)
        MainWindow.setTabOrder(self.button_search, self.textf_stuff)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приём заявок"))
        # self.lab_start_phone.setText(_translate("MainWindow", "+7"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d/M/yy"))
        self.lab_stuff.setText(_translate("MainWindow", "Примечания"))
        self.lab_phone.setText(_translate("MainWindow", "Телефон"))
        self.lab_product_name.setText(_translate("MainWindow", "Название изделия"))
        self.lab_date.setText(_translate("MainWindow", "Дата"))
        self.button_proceed.setText(_translate("MainWindow", "Принять в ремонт"))
        self.lab_receiver.setText(_translate("MainWindow", "Принял"))
        self.button_search.setText(_translate("MainWindow", "Поиск по базе"))
        self.lab_name.setText(_translate("MainWindow", "ФИО"))
        for i in list(enumerate(db.Receivers.find())):
            self.cBox_receiver.setItemText(i[0], _translate("MainWindow", i[1]['ФИО']))
        self.checkBox_guarantee.setText(_translate("MainWindow", "Гарантия"))

