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


# для файла первичной конфигурации
# cd \Program Files\MongoDB\Server\3.2\bin
# mongo.exe db-mydb --eval "db.yourCollection.insert({key:'value'})"
# pause

# import xlsx


def server():
    # путь прописывается индивидуально, либо
    # при значении пути по умолчанию аргумент опускается
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
        self.ui.line_phone.setText(phone)

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
                                    'Место': '', 
                                    'Передал в ремонт': '',
                                    'Работнику': '',
                                    'Перечень работ': '',
                                    'Дата зав': '',
                                    'Статус': ''})
        self.update_client()            
        globals()['sew'].create_table()
        self.win_clear()
        SuccessWin.initUI(globals()['suw'])

    def update_client(self):
        if db.Applicants.find_one({'Клиент': self.name 
            }) and not db.Applicants.find_one({u'Клиент': self.name, 
            'Телефон': self.phone}):
            temp_phone = '+7 ' + db.Applicants.find_one({'Клиент': self.name })[
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
            db.Applicants.insert_one({'Клиент': self.name, 
                                      'Телефон': self.phone})
            self.reset_completers() 

    def reset_completers(self):
        self.list_name = get_completer_data('client')
        self.completer = QtWidgets.QCompleter(self.list_client[0])
        self.completer_p = QtWidgets.QCompleter(self.list_client[1])
        self.ui.line_phone.setCompleter(self.completer_p)
        self.ui.line_name.setCompleter(self.completer)
        self.completer.activated.connect(self.complete_phone)
                  
    def check_func(self):
        while True:
            pattern_phone = r'[0-9]'
            self.product_name = r'{}'.format(self.ui.line_product_name.text())
            self.name = r'{}'.format(self.ui.line_name.text())
            self.receiver = r'{}'.format(str(self.ui.cBox_receiver.currentText()))
            self.stuff = r'{}'.format(self.ui.textf_stuff.toPlainText())
            self.phone = r'{}'.format(self.ui.line_phone.text())
            if self.product_name == '':
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
        globals()['myapp'].hide()
        globals()['sew'].show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.check_func()


class SearchWin(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_SearchWin()
        self.ui.setupUi(self)
        self.create_table()
        self.ui.search_button.clicked.connect(self.create_table)
        self.ui.add_button.clicked.connect(self.add_item)
        self.ui.delete_button.clicked.connect(self.are_you_sure)

    def get_data(self,search_word='',search_where='Заявки',
                order='Сначала новые'):
        datalist = []
        data_option = {
            'Заявки': {
            'header':['ФИО', 'Телефон', 'Изделие', 'Примечания', 'Дата', 
                    'Принял', 'Место', 'Передал в ремонт', 'Работнику', 
                    'Перечень работ', 'Дата зав', 'Статус', '_id'], 
            'db_func': db.Applications.find, 
            'filling_func': lambda i: [i['ФИО'], '+7 ' + str(i['Телефон']),
                    i['Изделие'],
                    i['Примечания'], str(i['Дата'])[6:] + '/' +
                    str(i['Дата'])[4:6] + '/' + 
                    str(i['Дата'])[0:4], i['Принял'], 
                    i['Место'], i['Передал в ремонт'], 
                    i['Работнику'], i['Перечень работ'], 
                    str(i['Дата зав'])[6:] + '/' +
                    str(i['Дата зав'])[4:6] + '/' + 
                    str(i['Дата зав'])[0:4], i['Статус'], 
                    str(i['_id'])]},
            'Клиенты': {
            'header': ['Клиент', 'Телефон', '_id'],
            'db_func': db.Applicants.find, 
            'filling_func': lambda i: [i['Клиент'], '+7 '+i['Телефон'], 
            str(i['_id'])]},
            'Работники': {
            'header': ['ФИО', '_id'],
            'db_func': db.Workers.find,
            'filling_func': lambda i: [i['ФИО'], str(i['_id'])]},
            'Приёмщики склада': {
            'header': ['ФИО', '_id'],
            'db_func': db.Receivers.find,
            'filling_func': lambda i: [i['ФИО'], str(i['_id'])]},
            'Операции' : {
            'header': ['Наименование', 'Цена', '_id'],
            'db_func': db.Jobs.find,
            'filling_func': lambda i: [i['Наименование'], i['Цена'], 
            str(i['_id'])]},
            'Изделия': {
            'header': ['Изделия', '_id'],
            'db_func': db.Prods.find,
            'filling_func': lambda i: [i['Изделие'], str(i['_id'])]}}
        self.db_func_arg_decorator(search_word, 
            data_option[search_where]['header'], 
            data_option[search_where]['db_func'], 
            data_option[search_where]['filling_func'], datalist, order)
        return [datalist, data_option[search_where]['header']]

    def db_func_arg_decorator(self, search_word, header, db_func, filling_func, 
                            datalist, order):
        if search_word == '':
            for i in db_func():
                tempvar = filling_func(i)
                self.choose_order(order, tempvar, datalist)
        else:
            for x in header:
                for i in db_func({ x : search_word}):
                    tempvar = filling_func(order, datalist, i)
                    self.choose_order(order, tempvar, datalist)

    def choose_order(self, order, tempvar, datalist):
        if order == 'Сначала старые':
            datalist.append(tempvar)
        elif order == 'Сначала новые':
            datalist.insert(0, tempvar)

    def create_table(self):
        self.word = self.ui.line_search.text()
        self.where = self.ui.comboBox_search_where.currentText()
        self.order = self.ui.comboBox_sort.currentText()
        datalist = self.get_data(self.word, self.where, self.order)
        self.table_model = ApplicationsTableModel(datalist[0], datalist[1], self, 
            table = self.where)
        self.ui.tableView_applications.setModel(self.table_model)
        data_option = {'Заявки':[1, 3, 6, 7, 8, 9, 10, 11], 'Клиенты':[0,1], 
        'Работники':[0], 'Приёмщики склада':[0],'Изделия':[0], 'Операции':[0,1]}
        for i in data_option[self.where]:
                self.ui.tableView_applications.setItemDelegateForColumn(i, 
                    Delegate(self, table = self.where))
        self.ui.tableView_applications.resizeColumnsToContents()
        self.ui.tableView_applications.horizontalHeader().setStretchLastSection(
            True)

    def add_item(self):
        self.where = self.ui.comboBox_search_where.currentText()
        if self.where == 'Заявки':
            globals()['sew'].hide()
            globals()['myapp'].show()
        else:
            pass

    def are_you_sure(self):
        msg = 'Вы точно хотите удалить \nэту запись?'
        reply = QtWidgets.QMessageBox.question(self, 'Внимание', 
                     msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.delete_item()
        elif reply == QtWidgets.QMessageBox.No:
            pass

    def delete_item(self):
        index = self.ui.tableView_applications.currentIndex()
        data_option = {'Заявки': {
        'identification' : index.sibling(index.row(), 12).data, 
        'del_func' : db.Applications.delete_one},
        'Клиенты': {
        'identification': index.sibling(index.row(), 2).data,
        'del_func' : db.Applicants.delete_one},
        'Работники': {
        'identification': index.sibling(index.row(), 1).data,
        'del_func' : db.Workers.delete_one},
        'Приёмщики склада': {
        'identification' : index.sibling(index.row(), 1).data,
        'del_func' : db.Receivers.delete_one},
        'Операции': {
        'identification' : index.sibling(index.row(), 2).data,
        'del_func' : db.Jobs.delete_one},
        'Изделия': {
        'identification' : index.sibling(index.row(), 1).data,
        'del_func' : db.Prods.delete_one}}
        data_option[self.where]['del_func']({
            '_id': ObjectId(data_option[self.where]['identification']())})
        self.create_table()


class ApplicationsTableModel(QtCore.QAbstractTableModel):

    def __init__(self, datain, headerdata, parent = None, table = 'Заявки'):
        # Datain is list of lists tabledata, headerdata is a string list
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata
        self.table = table

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.headerdata)

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and \
        role == QtCore.Qt.DisplayRole:
            try:
                return QtCore.QVariant(self.headerdata[section])
            except IndexError:                                                  # ДОИСПРАВЛЯТЬ ОШИБКУ
                self.columnCount(None, x=3)
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
        data_option = {'Заявки':[1, 3, 6, 7, 8, 9, 10, 11], 'Клиенты':[0,1], 
        'Работники':[0], 'Приёмщики склада':[0],'Изделия':[0], 'Операции':[0,1]}
        if index.column() in data_option[self.table]: # List of editable columns
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled |\
                QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


class Delegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent, table = 'Заявки'):
        QtWidgets.QStyledItemDelegate.__init__(self, parent)
        self.table = table

    def createEditor(self, parent, options, index):                             # ПЕРЕПИСАТЬ 
        data_option = {
        'Заявки': { 
        1: lambda parent: QtWidgets.QLineEdit(parent),
        3: lambda parent: QtWidgets.QPlainTextEdit(parent),
        6: lambda parent: self.combo_editor('Место', db.Places.find, parent), 
        7: lambda parent: self.combo_editor('ФИО', db.Receivers.find, parent),
        8: lambda parent: self.combo_editor('ФИО', db.Workers.find, parent), 
        9: lambda parent: self.job_line(parent),
        10: lambda parent: self.date_editor(parent)}, 
        'Клиенты': {
        0: lambda parent: QtWidgets.QLineEdit(parent),
        1: lambda parent: QtWidgets.QLineEdit(parent)}, 
        'Работники': { 
        0: lambda parent: QtWidgets.QLineEdit(parent)}, 
        'Приёмщики склада': {
        0: lambda parent: QtWidgets.QLineEdit(parent)},
        'Изделия': {
        0: lambda parent: QtWidgets.QLineEdit(parent)}, 
        'Операции': {
        0: lambda parent: QtWidgets.QLineEdit(parent),
        1: lambda parent: QtWidgets.QLineEdit(parent)}}
        return data_option[self.table][index.column()](parent)

    def combo_editor(self, field, func, parent):
        combo = QtWidgets.QComboBox(parent)
        li = []
        for i in func():
            li.append(i[field])
        combo.addItems(li)
        return combo

    def job_line(self, parent):
        line_jobs_done = QtWidgets.QLineEdit(parent)
        self.list_of_jobs = []
        for i in db.Jobs.find():
            self.list_of_jobs.append(i['Наименование'])
        completer = Completer(self.list_of_jobs)
        line_jobs_done.setCompleter(completer)
        return line_jobs_done

    def date_editor(self, parent):
        dateEdit = QtWidgets.QDateEdit(parent)
        dateEdit.setAutoFillBackground(False)
        dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateEdit.setCalendarPopup(True)
        return dateEdit

    def setEditorData(self, editor, index):                                     # ПЕРЕПИСАТЬ
        data_option = {
        'Заявки': { 
        1: lambda editor, index: editor.setText(index.data()[3:]),
        3: lambda editor, index: editor.setPlainText(index.data()),
        6: lambda editor, index: self.combo_editor_set(editor), 
        7: lambda editor, index: self.combo_editor_set(editor),
        8: lambda editor, index: self.combo_editor_set(editor), 
        9: lambda editor, index: editor.setText(index.data()) ,
        10: lambda editor, index: editor.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)},
        'Клиенты': {
        0: lambda editor, index: editor.setText(index.data()),
        1: lambda editor, index: editor.setText(index.data())}, 
        'Работники': { 
        0: lambda editor, index: editor.setText(index.data())}, 
        'Приёмщики склада': {
        0: lambda editor, index: editor.setText(index.data())},
        'Изделия': {
        0: lambda editor, index: editor.setText(index.data())}, 
        'Операции': {
        0: lambda editor, index: editor.setText(index.data()),
        1: lambda editor, index: editor.setText(index.data())}}
        print(self.table)
        print(index.column())
        column = index.column()
        data_option[self.table][index.column()](editor, index)

    def combo_editor_set(self, editor):
        editor.blockSignals(True)
        editor.setCurrentIndex(0)
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        data_option={'Заявки': {
        'identification' : model.index(index.row(),12).data, 
        'upd_func' : db.Applications.find_one_and_update, 
        3: {'new_data_func': lambda editor: editor.toPlainText(), 'field': 'Примечания'},
        1: {'new_data_func': lambda editor: self.new_data_phones(editor), 'field': 'Телефон'},
        6: {'new_data_func': lambda editor: editor.currentText(), 'field': 'Место'},
        7: {'new_data_func': lambda editor: editor.currentText(), 'field': 'Передал в ремонт'},
        8: {'new_data_func': lambda editor: editor.currentText(), 'field': 'Работнику'},
        9: {'new_data_func': lambda editor: self.new_data_jobs(editor), 'field': 'Перечень работ'},
        10:{'new_data_func': lambda editor: self.new_data_date(editor), 'field': 'Дата зав'}},
        'Клиенты': {
        'identification': model.index(index.row(), 2).data,
        'upd_func' : db.Applicants.find_one_and_update,
        0: {'new_data_func': lambda editor: editor.text(), 'field': 'Клиент'},
        1: {'new_data_func': lambda editor: self.new_data_phones(editor), 'field': 'Телефон'}},
        'Работники': {
        'identification': model.index(index.row(), 1).data,
        'upd_func' : db.Workers.find_one_and_update,
        0: {'new_data_func': lambda editor: editor.text(), 'field': 'ФИО'}},
        'Приёмщики склада': {
        'identification' : model.index(index.row(), 1).data,
        'upd_func' : db.Receivers.find_one_and_update,
        0: {'new_data_func': lambda editor: editor.text(), 'field': 'ФИО'}},
        'Операции': {
        'identification' : model.index(index.row(), 2).data,
        'upd_func' : db.Jobs.find_one_and_update, 
        0: {'new_data_func': lambda editor: editor.text(), 'field': 'Наименование'},
        1: {'new_data_func': lambda editor: self.new_data_prices(editor), 'field': 'Цена'}},
        'Изделия': {
        'identification' : model.index(index.row(), 1).data,
        'upd_func' : db.Prods.find_one_and_update,
        0: {'new_data_func': lambda editor: editor.text(), 'field': 'Изделие'}}}

        identification = data_option[self.table]['identification']()
        new_data = data_option[self.table][index.column()]['new_data_func'](editor)
        data_option[self.table]['upd_func']({'_id': ObjectId(identification)}, 
            {'$set':{data_option[self.table][index.column()]['field']:new_data}})
        globals()['sew'].create_table()

    def new_data_jobs(self, editor):
        new_data = editor.text()
        for i in new_data.split(', '):
            if not i in self.list_of_jobs:
                return ErrorJobName.initUI(globals()['erj'])
        return new_data

    def new_data_date(self, editor):
        temp_var = editor.date()
        new_data = int(str(temp_var.toPyDate())[0:4] +\
                 str(temp_var.toPyDate())[5:7] +\
                 str(temp_var.toPyDate())[8:])
        return new_data

    def new_data_phones(self, editor):
        new_data = editor.text()
        if not re.match(r'[0-9]', new_data) or len(new_data)!=10:
            ErrorWinPhone.initUI(globals()['erp'])
            return ''
        else:
            return new_data

    def new_data_prices(self, editor):
        new_data = editor.text()
        try:
            return float(new_data)
        except ValueError:
            ErrorJobPrice.initUI(globals()['ejp'])
            return 0


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
        globals()['myapp'] = MyWin()
        globals()['ern'] = ErrorWinName()
        globals()['erp'] = ErrorWinPhone()
        globals()['ers'] = ErrorWinStuff()
        globals()['ewp'] = ErrorWinProdName()
        globals()['suw'] = SuccessWin()
        globals()['sew'] = SearchWin()
        globals()['erj'] = ErrorJobName()
        globals()['ejp'] = ErrorJobPrice()
        globals()['myapp'].show()
        sys.exit(app.exec_())

thread_server = threading.Thread( target = server, name = 'server')
thread_main = threading.Thread( target = main_cycle, name = 'main cycle')

thread_server.start()
thread_main.start()

thread_server.join()
thread_main.join()