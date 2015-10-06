# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1096, 765)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 250, 850, 81))
        self.label.setStyleSheet(_fromUtf8("font: 75 28pt \"MS Shell Dlg 2\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(180, 390, 211, 41))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 440, 211, 41))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 490, 211, 41))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(180, 540, 211, 41))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 620, 151, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Question", None))
        self.radioButton.setText(_translate("Form", "RadioButton", None))
        self.radioButton_2.setText(_translate("Form", "RadioButton", None))
        self.radioButton_3.setText(_translate("Form", "RadioButton", None))
        self.radioButton_4.setText(_translate("Form", "RadioButton", None))
        self.pushButton.setText(_translate("Form", "Submit", None))


if __name__ == "__main__":
    import sys
    import random
    import string
    
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    WORDLIST_FILENAME = "GREwords.txt"
    def loadWords():
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = string.split(line)
        print "  ", len(wordlist), "words loaded."
        return wordlist
    def chooseWord(wordlist):
        """
        wordlist (list): list of words (strings)

        Returns a word from wordlist at random
        """
        return random.choice(wordlist)
    # Load the list of words into the variable wordlist
    # so that it can be accessed from anywhere in the program
    wordlist = loadWords()

    secretWord = chooseWord(wordlist).lower()
    ui.label.setText("What is the meaning of the word "+secretWord+"?")
    sys.exit(app.exec_())
