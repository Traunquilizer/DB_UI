import threading
import re
import sys
import os
import pymongo
from bson.objectid import ObjectId
# Импортируем наш интерфейс из файла
from name import *
from searchwin import *
from dialogwins import *
from PyQt5 import QtCore, QtGui, QtWidgets

client = pymongo.MongoClient()
db = client.Architecht

def server():
    '''путь прописывается индивидуально, либо
    при значении пути по умолчанию аргумент опускается'''
    os.system('mongod'+' --dbpath /var/lib/mongodb')


class MyWin(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.list_client = get_data('client')
        self.completer = QtWidgets.QCompleter(self.list_client[0])        
        self.ui.line_name.setCompleter(self.completer)
        self.completer_p = QtWidgets.QCompleter(self.list_client[1])
        self.ui.line_phone.setCompleter(self.completer_p)

        # вставить в файл интерфейса
        # self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.dateEdit.setCalendarPopup(True)

        self.completer.activated.connect(self.complete_phone)
        self.ui.button_proceed.clicked.connect(self.check_func)
        self.ui.button_search.clicked.connect(self.search_func)

    def complete_phone(self):
        self.name = self.ui.line_name.text()
        phone = db.Applicants.find_one({'Клиент': self.name})['Телефон']    
        #ДУБЛИРУЮТСЯ ДАННЫЕ! ПЕРЕПИСАТЬ!
        self.ui.line_phone.setText(phone)
        return print(phone)

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
        db.Applications.insert_one({u'ФИО': self.name,
                                    u'Телефон': self.phone,
                                    u'Принял': self.receiver,
                                    u'Изделие': self.product_name, 
                                    u'Примечания': self.stuff,
                                    u'Дата': date,
                                    u'Местоположение': '', 
                                    u'Передал в ремонт': '',
                                    u'Работнику': '',
                                    u'Перечень работ': '',
                                    u'Дата завершения': '',
                                    u'Статус': ''})
        # ПОПРОБОВАТЬ РЕАЛИЗОВАТЬ ОБНОВЛЕНИЕ СТАРЫХ ЗАПИСЕЙ
        if not db.Applicants.find_one({'Клиент': self.name, 
                                       'Телефон': self.phone}):
            db.Applicants.insert_one({u'Клиент': self.name, 
                                      u'Телефон': self.phone})
            self.reset_completers()
        globals()['sew'].create_table()
        self.win_clear()
        SuccessWin.initUI(globals()['suw'])

    def reset_completers(self):
        self.list_name = get_data('client')
        self.completer = QtWidgets.QCompleter(self.list_client[0])        
        self.ui.line_name.setCompleter(self.completer)
                  
    def check_func(self):
        while True:
            pattern_phone = r'[0-9]'
            self.product_name = self.ui.line_product_name.text()
            self.name = self.ui.line_name.text()
            self.receiver = str(self.ui.cBox_receiver.currentText())
            self.stuff = self.ui.textf_stuff.toPlainText()
            self.phone = self.ui.line_phone.text()
            if self.product_name == '' :
                ErrorWinProdName.initUI(globals()['ewp'])
                break               
            elif not re.match( r'^\w+[ ]\w+[ ]?\w+?$', self.name):
                ErrorWinName.initUI(globals()['ern'])
                break 
            elif not re.match(pattern_phone, self.phone) or len(self.phone)!=10:
                ErrorWinPhone.initUI(globals()['erp'])
                break
            elif self.stuff == '' :
                ErrorWinStuff.initUI(globals()['ers'])
                break
            self.insert_func()
            break

    def search_func(self):
        globals()['sew'].show()


# ПОДУМАТЬ НАСЧЕТ УТОЧНЯЮЩЕГО ПАРАМЕТРА И ЕГО РЕАЛИЗАЦИИ
def get_data(model_type):
    list_model = []
    if model_type== 'client':
        alist = []
        for i in db.Applicants.find():
            list_model.append(i['Клиент'])
            alist.append(i['Телефон'])
        return [list_model, alist]
    elif model_type == 'prod':
        for i in db.Prods.find():
            list_model.append(i['Изделие'])
        return list_model


class SearchWin(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SearchWin()
        self.ui.setupUi(self)
        self.create_table()     

        # НАПИСАТЬ ПОИСК
    def get_data(self):
        datalist = []
        for i in db.Applications.find():
            datalist.append([i['ФИО'], '+7 ' + str(i['Телефон']), i['Изделие'], 
                             i['Примечания'], str(i['Дата'])[6:] + '/' +
                             str(i['Дата'])[4:6] + '/' + 
                             str(i['Дата'])[0:4], i['Принял'], 
                             i['Местоположение'], i['Передал в ремонт'], 
                             i['Работнику'], i['Перечень работ'], 
                             i['Дата завершения'], i['Статус'], str(i['_id'])])
        return datalist

    def create_table(self):
        datalist = self.get_data()
        header = ['ФИО', 'Телефон', 'Изделие', 'Примечания', 'Дата', 'Принял', 
        'Место', 'Передал', 'Работнику', 'Перечень работ', 
        'Дата завершения', 'Статус', 'id']
        table_model = ApplicationsTableModel(datalist, header, self)
        self.ui.tableView_applications.setModel(table_model)
        self.ui.tableView_applications.setItemDelegateForColumn(3, 
            Delegate(self))


class ApplicationsTableModel(QtCore.QAbstractTableModel):

    def __init__(self, datain, headerdata, parent = None):
        # Datain is list of lists tabledata, headerdata is a string list
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return 13

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

    # ПЕРЕПИСАТЬ
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            if role == QtCore.Qt.EditRole:
                row = index.row()
                column = index.column()
                self.arraydata[row][column] = value
                return True
        return False

    def flags(self, index):
        if (index.column() == 3):
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled |\
            QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # ПЕРЕПИСАТЬ
    def resizeEvent(self, event):
    # Resize all sections to content and user interactive
        super(Table, self).resizeEvent(event)
        header = self.horizontalHeader()
        for column in range(header.count()):
            header.setSectionResizeMode(column, QHeaderView.ResizeToContents)
            width = header.sectionSize(column)
            header.setSectionResizeMode(column, QHeaderView.Interactive)
            header.resizeSection(column, width)


class Delegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent):
        QtWidgets.QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, options, index):
        return QtWidgets.QPlainTextEdit(parent)

    def setEditorData(self, editor, index):
        editor.setPlainText(index.data())

    # ДОПИСАТЬ!
    def setModelData(self, editor, model, index):
        # model.setData(index, editor.toPlainText())
        identification = model.index(index.row(), 12).data()
        new_data = editor.toPlainText()
        # if index.column == примечания:

        db.Applications.find_one_and_update({'_id': ObjectId(identification)}, 
            { '$set' : {'Примечания': new_data}})

        #, return_document = ReturnDocument.AFTER)

        # elif ... the rest of columns the same way
        a = db.Applications.find_one({'_id': ObjectId(identification)})
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