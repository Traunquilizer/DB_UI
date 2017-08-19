import threading
import re
import sys
import os
import pymongo
from bson.objectid import ObjectId
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
            self.ui.textf_stuff.setPlainText('')
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

        if not db.Applicants.find_one({u'Клиент': self.name, 
                                       u'Телефон': self.phone}):
            db.Applicants.insert_one({u'Клиент': self.name, 
                                      u'Телефон': self.phone})

        globals()['sew'].create_table()

        self.win_clear()
        SuccessWin.initUI(globals()['suw'])
                  
    def check_func(self):
        while True:
            pattern_phone = r'[0-9]{10}'
            self.product_name = self.ui.line_product_name.text()
            self.name = self.ui.line_name.text()
            self.receiver = str(self.ui.cBox_receiver.currentText())
            self.stuff = self.ui.textf_stuff.toPlainText()
            self.phone = self.ui.line_phone.text()
            if not re.match( r'^\w+[ ]\w+[ ]?\w+?$', self.name):
                ErrorWinName.initUI(globals()['ern'])
                break 
            elif self.product_name == '' :
                ErrorWinProdName.initUI(globals()['ewp'])
                break               
            elif not re.match(pattern_phone, self.phone):
                ErrorWinPhone.initUI(globals()['erp'])
                break
            elif self.stuff == '' :
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
        self.create_table()     

    def get_data(self):
        datalist = []
        for i in db.Applications.find():
            datalist.append([i['ФИО'], '+7 ' + str(i['Телефон']), i['Изделие'], 
                             i['Примечания'], str(i['Дата'])[6:] + '/' +
                             str(i['Дата'])[4:6] + '/' + 
                             str(i['Дата'])[0:4], i['Принял'], str(i['_id'])])
        return datalist

    def create_table(self):
        datalist = self.get_data()
        header = ['ФИО', 'Телефон', 'Изделие', 'Примечания', 'Дата', 'Принял', 
        'id']
        model = ApplicationsTableModel(datalist, header, self)
        self.ui.tableView_applications.setModel(model)
        self.ui.tableView_applications.setItemDelegateForColumn(3, Delegate(self))


class ApplicationsTableModel(QtCore.QAbstractTableModel):

    def __init__(self, datain = [['11', '12'], ['21', '22']], \
        headerdata = ['head1', 'head2'], parent = None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

# ПЕРЕОПРЕДЕЛИТЬ!
    def columnCount(self, parent):
        if len(self.arraydata) > 0: 
            return len(self.arraydata[0]) 
        return 0

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and \
        role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[section])
        elif orientation == QtCore.Qt.Vertical and \
        role == QtCore.Qt.DisplayRole:
            return QtCore.QAbstractTableModel.headerData(self, section, \
                orientation, role)
    
    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self.arraydata[index.row()][index.column()])

    def flags(self, index):
        if (index.column() == 3):
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled |\
            QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

# QtWidgets.QItemDelegate

class Delegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent):
        QtWidgets.QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, options, index):
        return QtWidgets.QPlainTextEdit(parent)

    def setEditorData(self, editor, index):
        editor.setPlainText(index.data())

    def setModelData(self, editor, model, index):
        # model.setData(index, editor.toPlainText())
        identification = model.index(index.row(), 6).data()
        new_data = editor.toPlainText()
        db.Applications.find_one_and_update({'_id': ObjectId(identification)}, 
            { '$set' : {'Примечания': new_data}})
        #, return_document = ReturnDocument.AFTER)
        a = db.Applications.find_one({'_id': ObjectId(identification)})
        print(str(a))
        print(editor.toPlainText())
        print(str(identification))
        globals()['sew'].create_table()


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