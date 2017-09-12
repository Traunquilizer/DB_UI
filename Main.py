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

'''
для файла первичной конфигурации
cd \Program Files\MongoDB\Server\3.2\bin
mongo.exe db-mydb --eval "db.yourCollection.insert({key:'value'});"
pause
'''

def server():
    '''путь прописывается индивидуально, либо
    при значении пути по умолчанию аргумент опускается'''
    os.system('mongod'+' --dbpath /var/lib/mongodb')


class MyWin(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.list_client = get_completer_data('client')
        self.completer = QtWidgets.QCompleter(self.list_client[0])        
        self.ui.line_name.setCompleter(self.completer)
        self.completer_p = QtWidgets.QCompleter(self.list_client[1])
        self.ui.line_phone.setCompleter(self.completer_p)

        # вставить в файл интерфейса
        # self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.dateEdit.setCalendarPopup(True)

        self.ui.button_proceed.clicked.connect(self.check_func)
        self.ui.button_search.clicked.connect(self.search_func)
        self.completer.activated.connect(self.complete_phone)

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
        db.Applications.insert_one({'ФИО': self.name,
                                    'Телефон': self.phone,
                                    'Принял': self.receiver,
                                    'Изделие': self.product_name, 
                                    'Примечания': self.stuff,
                                    'Дата': date,
                                    'Местоположение': '', 
                                    'Передал в ремонт': '',
                                    'Работнику': '',
                                    'Перечень работ': '',
                                    'Дата завершения': '',
                                    'Статус': ''})
        self.update_client()            
        globals()['sew'].create_table()
        self.win_clear()
        SuccessWin.initUI(globals()['suw'])

    def update_client(self):
        if db.Applicants.find_one({'Клиент': self.name 
            }) and not db.Applicants.find_one({u'Клиент': self.name, 
            'Телефон': self.phone}):
            temp_phone = '+7' + db.Applicants.find_one({'Клиент': self.name })[
            'Телефон']
            msg = 'Найдена запись \nКлиент: {}\nНомер: {}\n\n\nОбновить номер?'\
            .format(self.name, temp_phone)
            reply = QtWidgets.QMessageBox.question(self, 'Сообщение', 
                     msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                db.Applicants.find_one_and_update({'Клиент': self.name },{
                    '$set': {'Телефон': self.phone}})
                print(db.Applicants.find_one({u'Клиент': self.name, 
            'Телефон': self.phone}))
                self.reset_completers()
            elif reply == QtWidgets.QMessageBox.No:
                pass
        elif not db.Applicants.find_one({'Клиент': self.name }):
            db.Applicants.insert_one({u'Клиент': self.name, 
                                      u'Телефон': self.phone})
            self.reset_completers() 

    def reset_completers(self):
        self.list_name = get_data('client')
        self.completer = QtWidgets.QCompleter(self.list_client[0])
        self.completer_p = QtWidgets.QCompleter(self.list_client[1])
        self.ui.line_phone.setCompleter(self.completer_p)
        self.ui.line_name.setCompleter(self.completer)
        self.completer.activated.connect(self.complete_phone)
                  
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

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.check_func()


class SearchWin(QtWidgets.QMainWindow):                                         # НАПИСАТЬ ОТДЕЛЬНУЮ ФУНКЦИЮ ПОИСКА

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SearchWin()
        self.ui.setupUi(self)
        self.create_table()
        self.ui.search_button.clicked.connect(self.create_table)
        # self.ui.add_button.clicked.connect(self.add_func)

        # НАПИСАТЬ ПОИСК (self, arg = none, where =none):if arg and where==none:
    def get_data(self, search_word = '', search_where = 'Заявки', order = 'Сначала новые'):
        datalist = []
        if search_where == 'Заявки':
            header = ['ФИО', 'Телефон', 'Изделие', 'Примечания', 'Дата', 
            'Принял', 'Место', 'Передал', 'Работнику', 'Перечень работ', 
            'Дата зав.', 'Статус', 'id']
            if search_word == '':
                for i in db.Applications.find():
                    tempvar = [i['ФИО'], '+7 ' + str(i['Телефон']),
                                 i['Изделие'], 
                                 i['Примечания'], str(i['Дата'])[6:] + '/' +
                                 str(i['Дата'])[4:6] + '/' + 
                                 str(i['Дата'])[0:4], i['Принял'], 
                                 i['Местоположение'], i['Передал в ремонт'], 
                                 i['Работнику'], i['Перечень работ'], 
                                 str(i['Дата завершения'])[6:] + '/' +
                                 str(i['Дата завершения'])[4:6] + '/' + 
                                 str(i['Дата завершения'])[0:4], i['Статус'], 
                                 str(i['_id'])]
                    if order == 'Сначала старые':
                        datalist.append(tempvar)
                    elif order == 'Сначала новые':
                        datalist.insert(0, tempvar)
            # else:
                # for i in ['', '', '', '', '', '', '', '']
            
        elif search_where == 'Клиенты':
            for i in db.Applicants.find():
                tempvar = [i['Клиент'], '+7'+i['Телефон'], str(i['_id'])]
                if order == 'Сначала старые':
                    datalist.append(tempvar)
                elif order == 'Сначала новые':
                    datalist.insert(0, tempvar)
            header = ['Клиент', 'Телефон', 'id']
        return [datalist, header]

    def create_table(self):
        self.word = self.ui.line_search.text()
        self.where = self.ui.comboBox_search_where.currentText()
        self.order = self.ui.comboBox_sort.currentText()
        datalist = self.get_data(self.word, self.where, self.order)
        table_model = ApplicationsTableModel(datalist[0], datalist[1], self, table = self.where)
        self.ui.tableView_applications.setModel(table_model)
        if self.where == 'Заявки':
            self.ui.tableView_applications.setItemDelegateForColumn(3, 
                Delegate(self, table = self.where))
            for i in [6,7,8,9,10,11]:
                self.ui.tableView_applications.setItemDelegateForColumn(i, 
                    Delegate(self, table = self.where))
        elif self.where == 'Клиенты':
            for i in [0,1]:
                self.ui.tableView_applications.setItemDelegateForColumn(i, 
                    Delegate(self, table = self.where))
        self.ui.tableView_applications.resizeColumnsToContents()
        self.ui.tableView_applications.horizontalHeader().setStretchLastSection(
            True)

    # def add_func():
    #     self.where = self.ui.comboBox_search_where.currentText()
    #     addwin = AddWin(args)
    #     addwin.show()


class ApplicationsTableModel(QtCore.QAbstractTableModel):                       #ДОПИСАТЬ АРГУМЕНТ ВЫБОРА ТАБЛИЦЫ [WHOLE CLASS]

    def __init__(self, datain, headerdata, parent = None, table = 'Заявки'):
        # Datain is list of lists tabledata, headerdata is a string list
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata
        self.table = table

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

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
        
    def setData(self, index, value, role):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.arraydata[index.row()][index.column()] = QtCore.QVariant(value)
            self.emit(QtCore.SIGNAL("dataChanged(QModelIndex, QModelIndex)"), 
                index, index)
            return True
        else:
            return False

    def flags(self, index):
        if self.table == 'Заявки':
            if index.column() in [3, 6, 7, 8, 9, 10, 11]: # List of editable columns
                return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled |\
                QtCore.Qt.ItemIsSelectable
            else:
                return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        elif self.table == 'Клиенты':
            if index.column() in [0,1]:
                return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled |\
                QtCore.Qt.ItemIsSelectable
            else:
                return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


class Delegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent, table = 'Заявки'):                               #ДОПИСАТЬ АРГУМЕНТ ВЫБОРА ТАБЛИЦЫ [WHOLE CLASS]
        QtWidgets.QStyledItemDelegate.__init__(self, parent)
        self.table = table

    def createEditor(self, parent, options, index):
        if self.table == 'Заявки':
            if index.column() == 3:
                return QtWidgets.QPlainTextEdit(parent)
            elif index.column() in [6, 7, 8]:
                combo = QtWidgets.QComboBox(parent)
                li = []
                if index.column() == 6:
                    for i in db.Places.find():
                        li.append(i['Место'])
                elif index.column() == 7:
                    for i in db.Receivers.find():
                        li.append(i['ФИО'])
                elif index.column() == 8:
                    for i in db.Workers.find():
                        li.append(i['ФИО'])
                combo.addItems(li)
                return combo
            elif index.column() == 9:
                line_jobs_done = QtWidgets.QLineEdit(parent)
                self.list_of_jobs = []
                for i in db.Jobs.find():
                    self.list_of_jobs.append(i['Наименование'])
                completer = Completer(self.list_of_jobs)
                line_jobs_done.setCompleter(completer)
                return line_jobs_done
            elif index.column() == 10:
                dateEdit = QtWidgets.QDateEdit()
                # dateEdit.setGeometry(QtCore.QRect(100, 500, 110, 32))
                dateEdit.setAutoFillBackground(False)
                dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
                dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
                dateEdit.setCalendarPopup(True)
                return dateEdit
        elif self.table == 'Клиенты':
            if index.column() in [0, 1]:
                return QtWidgets.QLineEdit(parent)

    def setEditorData(self, editor, index):
        if self.table == 'Заявки':
            if index.column() == 3:
                editor.setPlainText(index.data())
            elif index.column() in [6,7,8]:
                editor.blockSignals(True)
                editor.setCurrentIndex(0)
                editor.blockSignals(False)
            elif index.column() == 9:
                editor.setText(index.data())
            elif index.column() == 10:
                editor.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        elif self.table == 'Клиенты':
            if index.column() == 0:
                editor.setText(index.data())
            if index.column() == 1:
                editor.setText(index.data())

    # ДОПИСАТЬ!
    def setModelData(self, editor, model, index):
        if self.table == 'Заявки':
            identification = model.index(index.row(), 12).data()        
            if index.column() == 3:
                new_data = editor.toPlainText()
                db.Applications.find_one_and_update({'_id': 
                    ObjectId(identification)}, 
                    { '$set' : {'Примечания': new_data}})
            elif index.column() == 6:
                new_data = editor.currentText()
                db.Applications.find_one_and_update({'_id':
                    ObjectId(identification)}, 
                    { '$set' : {'Местоположение': new_data}})
            elif index.column() == 7:
                new_data = editor.currentText()
                db.Applications.find_one_and_update({'_id':
                    ObjectId(identification)}, 
                    { '$set' : {'Передал в ремонт' : new_data}})
            elif index.column() == 8:
                new_data  = editor.currentText()
                db.Applications.find_one_and_update({'_id':
                    ObjectId(identification)}, 
                    { '$set' : {'Работнику' : new_data}})
            elif index.column() == 9:
                new_data = editor.text()
                for i in new_data.split(', '):
                    if not i in self.list_of_jobs:
                        return ErrorJobName.initUI(globals()['erj'])
                db.Applications.find_one_and_update({'_id':
                    ObjectId(identification)}, 
                    { '$set' : { 'Перечень работ' : new_data }})
            elif index.column() == 10:
                temp_var = editor.date()
                new_data = int(str(temp_var.toPyDate())[0:4] +\
                 str(temp_var.toPyDate())[5:7] +\
                 str(temp_var.toPyDate())[8:])
                db.Applications.find_one_and_update({ '_id' : 
                    ObjectId(identification)}, 
                    { '$set' : { 'Дата завершения' : new_data }})
            a = db.Applications.find_one({'_id': ObjectId(identification)})
        elif self.table == 'Клиенты':
            identification = model.index(index.row(), 2).data()  
            if index.column() == 0:
                new_data = editor.text()
                db.Applicants.find_one_and_update({ '_id' : 
                    ObjectId(identification)},{'$set' : { 'Клиент' : new_data}})
            elif index.column() == 1:
                new_data = editor.text()
                if not re.match(r'[0-9]', new_data) or len(new_data)!=10:
                    return ErrorWinPhone.initUI(globals()['erp'])
                db.Applicants.find_one_and_update({'_id':
                    ObjectId(identification)}, 
                    { '$set' : { 'Телефон': new_data}})
            a = db.Applicants.find_one({'_id': ObjectId(identification)})

        print(a)
        print(str(identification))
        globals()['sew'].create_table()


class Completer(QtWidgets.QCompleter):

    def __init__(self, parent=None):
        super(Completer, self).__init__(parent)

        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.setWrapAround(False)

    # Add texts instead of replace
    def pathFromIndex(self, index):
        path = QtWidgets.QCompleter.pathFromIndex(self, index)

        lst = str(self.widget().text()).split(',')

        if len(lst) > 1:
            path = '%s, %s' % (','.join(lst[:-1]), path)

        return path

    # Add operator to separate between texts
    def splitPath(self, path):
        path = str(path.split(',')[-1]).lstrip(' ')
        return [path]


# ПОДУМАТЬ НАСЧЕТ УТОЧНЯЮЩЕГО ПАРАМЕТРА И ЕГО РЕАЛИЗАЦИИ
def get_completer_data(model_type):
    list_model = []
    if model_type == 'client':
        alist = []
        for i in db.Applicants.find():
            list_model.append(i['Клиент'])
            alist.append(i['Телефон'])
        list_model = list(set(list_model))
        alist = list(set(alist))
        return [list_model, alist]
    elif model_type == 'prod':
        for i in db.Prods.find():
            list_model.append(i['Изделие'])
        return list_model


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
        globals()['erj'] = ErrorJobName()
        # globals()['dialogwin'] = QtWidgets.QMessageBox()
        myapp.show()
        sys.exit(app.exec_())


thread_server = threading.Thread( target = server, name = 'server')
thread_main = threading.Thread( target = main_cycle, name = 'main cycle')

thread_server.start()
thread_main.start()

thread_server.join()
thread_main.join()