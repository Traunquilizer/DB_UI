# import subprocess
import re
import sys
import os
import pymongo
import datetime
# from MyDictionaryCompleter import MyDictionaryCompleter
# Импортируем наш интерфейс из файла
from name import *
from PyQt5 import QtCore, QtGui, QtWidgets

# subprocess.call('mongod'+' --dbpath /var/lib/mongodb', shell = True)

client = pymongo.MongoClient()
db = client.Architecht


class MyWin(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # поставить в интерфейс
        # self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.dateEdit.setCalendarPopup(True)

        
        # Здесь прописываем событие нажатия на кнопку        
        self.ui.button_proceed.clicked.connect(self.check_func)

        self.ui.button_search.clicked.connect(self.search_func)

    def insert_func(self):
        temp_var = self.ui.dateEdit.date()
        date = int(str(temp_var.toPyDate())[0:4] + str(temp_var.toPyDate())[5:7] + str(temp_var.toPyDate())[8:])
        print(type(date))

        db.Applications.insert_one({u'ФИО': self.name,
                                    u'Телефон': self.phone,
                                    u'Принял': self.receiver,
                                    u'Изделие': self.product_name, 
                                    u'Примечания': self.stuff,
                                    u'Дата': date })
                  
    def check_func(self):
        error_ = ''
        pattern_phone = r'[0-9]{10}'
        self.product_name = self.ui.textf_product_name.toPlainText()
        self.name = self.ui.textf_name.toPlainText()
        self.receiver = str(self.ui.cBox_receiver.currentText())
        self.stuff = self.ui.textf_stuff.toPlainText()
        self.phone = self.ui.textf_phone.toPlainText()
        if not re.match( r'^\w+[ ]\w+[ ]?\w+?$', self.name):
            error_ = 'Неправильно введено ФИО'
        elif not re.match(pattern_phone, self.phone) or len(self.phone):
            error_ = 'Неправильно заполнен номер'
        elif self.stuff =='':
            error_ = 'Не введены примечания'
        elif self.product_name =='':
            error_ = 'Не введено название изделия'
        DialogWin.initUI(di)
        self.insert_func()


    def search_func(self):
        pass


class DialogWin(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # self.initUI()


    def initUI(self):

        self.btn = QtWidgets.QPushButton('OK', self)
        self.btn.move(50, 50)
        # self.btn.clicked.connect(self.showDialog)

        # self.le = QtWidgets.QLineEdit(self)
        # self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Error')
        self.show()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    di = DialogWin()
    sys.exit(app.exec_())