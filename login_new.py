# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sat Oct 31 20:12:19 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(949, 669)
        font = QtGui.QFont()
        font.setPointSize(17)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("QFrame{\n"
"background-image: url(:/prefix/Pictures/ubuntu12.04-login-screen.png);\n"
"}\n"
"QPushButton{\n"
"    font: 63 14pt \"Ubuntu\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgb(255, 255, 255)\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -20, 971, 711))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.password = QtGui.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(40, 300, 211, 41))
        self.password.setStyleSheet(_fromUtf8("background-color: transparent;;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 16pt \"Ubuntu\";\n"
"border-radius: 10px;"))
        self.password.setObjectName(_fromUtf8("password"))
        self.username = QtGui.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(40, 370, 211, 41))
        self.username.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 16pt \"Ubuntu\";\n"
"border-radius: 10px;"))
        self.username.setEchoMode(QtGui.QLineEdit.Password)
        self.username.setObjectName(_fromUtf8("username"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 430, 131, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.password.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.username.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.pushButton.setText(_translate("MainWindow", "Login", None))

import rs1
def submit():
    print "Prathamesh"
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(submit)
    MainWindow.show()
    sys.exit(app.exec_())
    
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #ui.pushButton.clicked.connect(submit)
    MainWindow.show()
    sys.exit(app.exec_())
    

