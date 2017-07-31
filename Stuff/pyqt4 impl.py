from PyQt4 import QtGui,QtCore
from mMyDictionaryCompleter import MyDictionaryCompleter
#===============================================================================
# MyTextEdit  
#===============================================================================
class MyTextEdit(QtGui.QTextEdit):
#|-----------------------------------------------------------------------------|
# class Variables
#|-----------------------------------------------------------------------------| 
    #no classVariables
#     myFocusOutSignal=QtCore.pyqtSignal(str)
#|-----------------------------------------------------------------------------|
# Constructor  
#|-----------------------------------------------------------------------------|
    def __init__(self,*args):
        #*args to set parent
        QtGui.QLineEdit.__init__(self,*args)
        font=QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.completer = None

#|--------------------------End of __init__------------------------------------|
#|-----------------------------------------------------------------------------| 
# setCompleter
#|-----------------------------------------------------------------------------|
    def setCompleter(self, completer):
        if self.completer:
            self.disconnect(self.completer, 0, self, 0)
        if not completer:
            return

        completer.setWidget(self)
        completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer = completer
#        self.connect(self.completer,
#            QtCore.SIGNAL("activated(const QString&)"), self.insertCompletion)
        self.completer.insertText.connect(self.insertCompletion)
#|-----------------------End of setCompleter-------------------------------------|
#|-----------------------------------------------------------------------------| 
# insertCompletion
#|-----------------------------------------------------------------------------|
    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (len(completion) -
            len(self.completer.completionPrefix()))
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)
#|-----------------------End of insertCompletion-------------------------------|
#|-----------------------------------------------------------------------------| 
# textUnderCursor
#|-----------------------------------------------------------------------------|
    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QtGui.QTextCursor.WordUnderCursor)
        return tc.selectedText()
#|-----------------------End of textUnderCursor--------------------------------|
#|-----------------------------------------------------------------------------| 
# focusInEvent
#|-----------------------------------------------------------------------------|
    #---override
    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self);
        QtGui.QTextEdit.focusInEvent(self, event)
#|-----------------------End of focusInEvent-------------------------------------|
#|-----------------------------------------------------------------------------| 
# keyPressEvent
#|-----------------------------------------------------------------------------|
    #---override
    def keyPressEvent(self, event):
        if self.completer and self.completer.popup() and self.completer.popup().isVisible():
            if event.key() in (
            QtCore.Qt.Key_Enter,
            QtCore.Qt.Key_Return,
            QtCore.Qt.Key_Escape,
            QtCore.Qt.Key_Tab,
            QtCore.Qt.Key_Backtab):
                event.ignore()
                return
        ## has ctrl-Space been pressed??
        isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and\
                      event.key() == QtCore.Qt.Key_Space)
        ## modifier to complete suggestion inline ctrl-e
        inline = (event.modifiers() == QtCore.Qt.ControlModifier and \
                  event.key() == QtCore.Qt.Key_E)
        ## if inline completion has been chosen
        if inline:
            # set completion mode as inline
            self.completer.setCompletionMode(QtGui.QCompleter.InlineCompletion)
            completionPrefix = self.textUnderCursor()
            if (completionPrefix != self.completer.completionPrefix()):
                self.completer.setCompletionPrefix(completionPrefix)
            self.completer.complete()
#            self.completer.setCurrentRow(0)
#            self.completer.activated.emit(self.completer.currentCompletion())
            # set the current suggestion in the text box
            self.completer.insertText.emit(self.completer.currentCompletion())
            # reset the completion mode
            self.completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
            return
        if (not self.completer or not isShortcut):
            pass
            QtGui.QTextEdit.keyPressEvent(self, event)
        # debug
#        print("After controlspace")
#        print("isShortcut is: {}".format(isShortcut))
        # debug over
        ## ctrl or shift key on it's own??
        ctrlOrShift = event.modifiers() in (QtCore.Qt.ControlModifier ,\
                QtCore.Qt.ShiftModifier)
        if ctrlOrShift and event.text()== '':
#             ctrl or shift key on it's own
            return
        # debug
#        print("After on its own")
#        print("isShortcut is: {}".format(isShortcut))
        # debug over
#         eow = QtCore.QString("~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-=") #end of word
#        eow = "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-=" #end of word
        eow = "~!@#$%^&*+{}|:\"<>?,./;'[]\\-=" #end of word

        hasModifier = ((event.modifiers() != QtCore.Qt.NoModifier) and\
                        not ctrlOrShift)

        completionPrefix = self.textUnderCursor()
#         print('event . text = {}'.format(event.text().right(1)))
#         if (not isShortcut and (hasModifier or event.text()=='' or\
#                                 len(completionPrefix) < 3 or \
#                                 eow.contains(event.text().right(1)))):
        if not isShortcut :
            if self.completer.popup():
                self.completer.popup().hide()
            return
#        print("complPref: {}".format(completionPrefix))
#        print("completer.complPref: {}".format(self.completer.completionPrefix()))
#        print("mode: {}".format(self.completer.completionMode()))
#        if (completionPrefix != self.completer.completionPrefix()):
        self.completer.setCompletionPrefix(completionPrefix)
        popup = self.completer.popup()
        popup.setCurrentIndex(
            self.completer.completionModel().index(0,0))
        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr) ## popup it up!
#|-----------------------End of keyPressEvent----------------------------------|

if __name__ == "__main__":

    app = QtGui.QApplication([])
    completer = MyDictionaryCompleter()
    te = MyTextEdit()
    te.setCompleter(completer)
    te.show()
    app.exec_()