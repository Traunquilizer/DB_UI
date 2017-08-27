from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, Qt

class ErrorWinName(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Неправильно введено ФИО' , self)
        self.lbl.move(35, 30)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape or e.key() == Qt.Key_Return:
            self.close()


class ErrorWinPhone(ErrorWinName):

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Неправильно введен номер' , self)
        self.lbl.move(35, 30)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class ErrorWinStuff(ErrorWinName):

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Не введены примечания' , self)
        self.lbl.move(35, 30)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class ErrorWinProdName(ErrorWinName):

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Не введено название изделия' , self)
        self.lbl.move(35, 30)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class ErrorJobName(ErrorWinName):

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Неправильно введено\n наименование работы' , self)
        self.lbl.move(40, 20)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Ошибка')
        self.show()


class SuccessWin(ErrorWinName):

    def initUI(self):
        self.lbl = QtWidgets.QLabel( 'Заявка успешно сохранена' , self)
        self.lbl.move(35, 30)

        self.setGeometry(700, 400, 250, 70)
        self.setWindowTitle('Выполнено')
        self.show()