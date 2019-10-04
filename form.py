# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 177)
        self.button_add = QtWidgets.QPushButton(Form)
        self.button_add.setGeometry(QtCore.QRect(150, 130, 101, 25))
        self.button_add.setObjectName("button_add")
        self.button_cancel = QtWidgets.QPushButton(Form)
        self.button_cancel.setGeometry(QtCore.QRect(260, 130, 91, 25))
        self.button_cancel.setObjectName("button_cancel")
        self.lineEdit_0 = QtWidgets.QLineEdit(Form)
        self.lineEdit_0.setGeometry(QtCore.QRect(20, 29, 331, 21))
        self.lineEdit_0.setObjectName("lineEdit_0")
        self.label_0 = QtWidgets.QLabel(Form)
        self.label_0.setGeometry(QtCore.QRect(20, 10, 58, 18))
        self.label_0.setObjectName("label_0")
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 79, 331, 21))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(20, 60, 58, 18))
        self.label_1.setObjectName("label_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_add.setText(_translate("Form", "Подтвердить"))
        self.button_cancel.setText(_translate("Form", "Отмена"))
        self.label_0.setText(_translate("Form", "TextLabel"))
        self.label_1.setText(_translate("Form", "TextLabel"))

