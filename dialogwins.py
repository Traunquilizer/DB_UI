from PyQt5 import QtWidgets

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