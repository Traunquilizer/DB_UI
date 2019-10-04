from PyQt5 import QtWidgets, QtCore


class ErrorWin(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.lbl = QtWidgets.QLabel( self.label , self)
        self.lbl.move(35, 30)
        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle(self.win_title)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape or e.key() == QtCore.Qt.Key_Return:
            self.close()


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
        self.label_0.setGeometry(QtCore.QRect(20, 10, 100, 18))
        self.label_0.setObjectName("label_0")
        
        if self.field_1:
                self.lineEdit_1 = QtWidgets.QLineEdit(Form)
                self.lineEdit_1.setGeometry(QtCore.QRect(20, 79, 331, 21))
                self.lineEdit_1.setObjectName("lineEdit_1")
                self.label_1 = QtWidgets.QLabel(Form)
                self.label_1.setGeometry(QtCore.QRect(20, 60, 100, 18))
                self.label_1.setObjectName("label_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Форма ввода записей в базу {}".format(self.db_name)))
        self.button_add.setText(_translate("Form", "Подтвердить"))
        self.button_cancel.setText(_translate("Form", "Отмена"))
        self.label_0.setText(_translate("Form", self.field_0))
        if self.field_1:
            self.label_1.setText(_translate("Form", self.field_1))