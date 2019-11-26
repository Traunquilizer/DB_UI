from PyQt5 import QtWidgets, QtCore


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.centralWidget = QtWidgets.QWidget(Form)
        self.centralWidget.setObjectName("Form")
        Form.setCentralWidget(self.centralWidget)
        self.formLayout = QtWidgets.QFormLayout(self.centralWidget)
        self.formLayout.setObjectName("formLayout")

    def creating_buttons(self, Form, counter):
        Form.resize(377, counter*50)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(counter, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        
    def create_fields(self, Form, counter, field_widget):
        a = 'field_' + str(counter)
        b = 'label_' + str(counter)
        self.__dict__[b] = QtWidgets.QLabel(Form)
        self.__dict__[b].setObjectName(b)
        self.formLayout.setWidget(counter, QtWidgets.QFormLayout.LabelRole, self.__dict__[b])
        self.__dict__[a] = field_widget
        self.__dict__[a].setObjectName(a)
        self.formLayout.setWidget(counter, QtWidgets.QFormLayout.FieldRole, self.__dict__[a])

    def start_retranslate(self, Form, disp_list):
        self.retranslateUi(Form, disp_list)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, disp_list):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.win_title))
        counter = 0
        for i in disp_list:
            a = 'label_' + str(counter)
            self.__dict__[a].setText(_translate("Form", i))
            counter+=1