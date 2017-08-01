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
# надо как-то заставить это работать отдельно, чтобы не запускать через батник

client = pymongo.MongoClient()
db = client.Architecht


class MyWin(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # вставить в файл интерфейса
        # self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.dateEdit.setCalendarPopup(True)

        
        # Здесь прописываем событие нажатия на кнопку        
        self.ui.button_proceed.clicked.connect(self.check_func)

        self.ui.button_search.clicked.connect(self.search_func)

    def insert_func(self):
        temp_var = self.ui.dateEdit.date()
        date = int(str(temp_var.toPyDate())[0:4] +\
         str(temp_var.toPyDate())[5:7] +\
         str(temp_var.toPyDate())[8:])
        print(type(date))

        db.Applications.insert_one({u'ФИО': self.name,
                                    u'Телефон': self.phone,
                                    u'Принял': self.receiver,
                                    u'Изделие': self.product_name, 
                                    u'Примечания': self.stuff,
                                    u'Дата': date })
                  
    def check_func(self):
        while True:
            pattern_phone = r'[0-9]{10}'
            self.product_name = self.ui.textf_product_name.toPlainText()
            self.name = self.ui.textf_name.toPlainText()
            self.receiver = str(self.ui.cBox_receiver.currentText())
            self.stuff = self.ui.textf_stuff.toPlainText()
            self.phone = self.ui.textf_phone.toPlainText()
            if not re.match( r'^\w+[ ]\w+[ ]?\w+?$', self.name):
                ErrorWinName.initUI(ern)
                break 
            elif self.product_name =='':
                ErrorWinProdName.initUI(ewp)
                break               
            elif not re.match(pattern_phone, self.phone):
                ErrorWinPhone.initUI(erp)
                break
            elif self.stuff =='':
                ErrorWinStuff.initUI(ers)
                break
            self.insert_func()
            break

    def search_func(self):
        pass


class ErrorWinName(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Неправильно введено ФИО' , self)
        self.lbl.move(20, 20)

        self.setGeometry(700, 400, 250, 100)
        self.setWindowTitle('Error')
        self.show()


class ErrorWinPhone(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Неправильно введен номер' , self)
        self.lbl.move(20, 20)

        self.setGeometry(700, 400, 250, 100)
        self.setWindowTitle('Error')
        self.show()


class ErrorWinStuff(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Не введены примечания' , self)
        self.lbl.move(20, 20)

        self.setGeometry(700, 400, 250, 100)
        self.setWindowTitle('Error')
        self.show()


class ErrorWinProdName(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Не введено название изделия' , self)
        self.lbl.move(20, 20)

        self.setGeometry(700, 400, 250, 100)
        self.setWindowTitle('Error')
        self.show()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    ern = ErrorWinName()
    erp = ErrorWinPhone()
    ers = ErrorWinStuff()
    ewp = ErrorWinProdName()
    sys.exit(app.exec_())