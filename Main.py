import threading
import re
import sys
import os
import pymongo
# Импортируем наш интерфейс из файла
from name import *
from searchwin import *
from PyQt5 import QtCore, QtGui, QtWidgets

client = pymongo.MongoClient()
db = client.Architecht

def server():
    # путь прописывается индивидуально, либо
    # при значении пути по умолчанию аргумент опускается
    os.system('mongod'+' --dbpath /var/lib/mongodb')


class MyWin(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # вставить в файл интерфейса
        # self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.dateEdit.setCalendarPopup(True)
        
        self.ui.button_proceed.clicked.connect(self.check_func)
        self.ui.button_search.clicked.connect(self.search_func)

    def win_clear(self):
            self.ui.line_product_name.setText('')
            self.ui.line_name.setText('')
            self.ui.line_stuff.setText('')
            self.ui.line_phone.setText('')

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
        self.win_clear()
        SuccessWin.initUI(globals()['suw'])
                  
    def check_func(self):
        while True:
            pattern_phone = r'[0-9]{10}'
            self.product_name = self.ui.line_product_name.text()
            self.name = self.ui.line_name.text()
            self.receiver = str(self.ui.cBox_receiver.currentText())
            self.stuff = self.ui.line_stuff.text()
            self.phone = self.ui.line_phone.text()
            if not re.match( r'^\w+[ ]\w+[ ]?\w+?$', self.name):
                ErrorWinName.initUI(globals()['ern'])
                break 
            elif self.product_name =='':
                ErrorWinProdName.initUI(globals()['ewp'])
                break               
            elif not re.match(pattern_phone, self.phone):
                ErrorWinPhone.initUI(globals()['erp'])
                break
            elif self.stuff =='':
                ErrorWinStuff.initUI(globals()['ers'])
                break
            self.insert_func()
            break

    def search_func(self):
        # SearchWin.initUI(globals()['sew'])
        globals()['sew'].show()


class ErrorWinName(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        # self.center()
        self.lbl = QtWidgets.QLabel( 'Неправильно введено ФИО' , self)
        self.lbl.move(40, 40)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class ErrorWinPhone(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        # self.center()
        self.lbl = QtWidgets.QLabel( 'Неправильно введен номер' , self)
        self.lbl.move(40, 40)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class ErrorWinStuff(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        # self.center()
        self.lbl = QtWidgets.QLabel( 'Не введены примечания' , self)
        self.lbl.move(40, 40)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class ErrorWinProdName(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        # self.center()
        self.lbl = QtWidgets.QLabel( 'Не введено название изделия' , self)
        self.lbl.move(40, 40)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class SuccessWin(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        # self.center()
        self.lbl = QtWidgets.QLabel( 'Заявка успешно сохранена' , self)
        self.lbl.move(40, 40)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Выполнено')
        self.show()



class SearchWin(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SearchWin()
        self.ui.setupUi(self)
#         super().__init__()

#     def initUI(self):
#         # self.centralWidget = QtWidgets.Qwidget(SearchWin)

#         col_headers = ['Изделие', 'ФИО', 'Телефон', 'Примечания', 
#         'Дата', 'Принял']
#         self.setGeometry(700, 400, 800, 500)
#         self.setWindowTitle('Заявки')
#         self.form_widget = SearchTable(50, 6)
#         self.form_widget.setHorizontalHeaderLabels(col_headers)
#         self.setCentralWidget(self.form_widget)
#         # self.lab_start_phone = QtWidgets.QLabel(self.centralWidget)
#         # self.lab_start_phone.setGeometry(QtCore.QRect(30, 220, 21, 31))
#         # self.lab_start_phone.setObjectName("lab_start_phone")
#         self.show()

# class SearchTable(QtWidgets.QTableWidget):

#     def __init__(self, r, c):
#         super().__init__(r, c)
#         self.initUI()

#     def initUI(self):
#         self.show()
        

def main_cycle():
    if __name__=="__main__":        
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        globals()['ern'] = ErrorWinName()
        globals()['erp'] = ErrorWinPhone()
        globals()['ers'] = ErrorWinStuff()
        globals()['ewp'] = ErrorWinProdName()
        globals()['suw'] = SuccessWin()
        globals()['sew'] = SearchWin()
        myapp.show()
        sys.exit(app.exec_())       

thread_server = threading.Thread( target = server, name = 'server')
thread_main = threading.Thread( target = main_cycle, name = 'main cycle')

thread_server.start()
thread_main.start()

thread_server.join()
thread_main.join()