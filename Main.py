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
        pattern_phone = r'[0-9]{10,10}'
        self.product_name = self.ui.textf_product_name.toPlainText()
        self.name = self.ui.textf_name.toPlainText()
        self.receiver = str(self.ui.cBox_receiver.currentText())
        self.stuff = self.ui.textf_stuff.toPlainText()
        self.phone = self.ui.textf_phone.toPlainText()
        if not re.match(pattern_phone, self.phone): # and len(self.phone):
            Example.showDialog(ex)
        elif self.stuff =='':
            pass
        elif self.name =='':
            pass
        elif self.product_name =='':
            pass
        self.insert_func()


    def search_func(self):
        pass


class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # self.initUI()


    def initUI(self):

        self.btn = QtWidgets.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        # self.btn.clicked.connect(self.showDialog)

        self.le = QtWidgets.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):

        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')
        if ok:
            self.le.setText(str(text))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    ex = Example()
    sys.exit(app.exec_())