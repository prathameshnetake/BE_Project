# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(944, 669)
        font = QtGui.QFont()
        font.setPointSize(17)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("QFrame#frame{\n"
"    background-image: url(:/prefix/Pictures/Assets/ubuntu12.04-login-screen.png);\n"
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
        self.frame.setGeometry(QtCore.QRect(-10, -10, 971, 711))
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.loginUsername = QtGui.QLineEdit(self.frame)
        self.loginUsername.setGeometry(QtCore.QRect(30, 40, 211, 41))
        self.loginUsername.setStyleSheet(_fromUtf8("background-color: transparent;;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 16pt \"Ubuntu\";\n"
"border-radius: 10px;"))
        self.loginUsername.setObjectName(_fromUtf8("loginUsername"))
        self.loginPassword = QtGui.QLineEdit(self.frame)
        self.loginPassword.setGeometry(QtCore.QRect(30, 90, 211, 41))
        self.loginPassword.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 16pt \"Ubuntu\";\n"
"border-radius: 10px;"))
        self.loginPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.loginPassword.setObjectName(_fromUtf8("loginPassword"))
        self.loginSubmit = QtGui.QPushButton(self.frame)
        self.loginSubmit.setGeometry(QtCore.QRect(30, 150, 131, 31))
        self.loginSubmit.setObjectName(_fromUtf8("loginSubmit"))
        self.signUpUsername = QtGui.QLineEdit(self.frame)
        self.signUpUsername.setGeometry(QtCore.QRect(290, 40, 281, 41))
        self.signUpUsername.setStyleSheet(_fromUtf8("background-color: transparent;;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 16pt \"Ubuntu\";\n"
"border-radius: 10px;"))
        self.signUpUsername.setObjectName(_fromUtf8("signUpUsername"))
        self.signUpPass = QtGui.QLineEdit(self.frame)
        self.signUpPass.setGeometry(QtCore.QRect(290, 100, 281, 41))
        self.signUpPass.setStyleSheet(_fromUtf8("background-color: transparent;;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 16pt \"Ubuntu\";\n"
"border-radius: 10px;"))
        self.signUpPass.setEchoMode(QtGui.QLineEdit.Password)
        self.signUpPass.setObjectName(_fromUtf8("signUpPass"))
        self.signUpEmail = QtGui.QLineEdit(self.frame)
        self.signUpEmail.setGeometry(QtCore.QRect(290, 160, 281, 41))
        self.signUpEmail.setStyleSheet(_fromUtf8("background-color: transparent;;\n"
"color: rgb(255, 255, 255);\n"
"font: 63 16pt \"Ubuntu\";\n"
"border-radius: 10px;"))
        self.signUpEmail.setObjectName(_fromUtf8("signUpEmail"))
        self.signUpSubmit = QtGui.QPushButton(self.frame)
        self.signUpSubmit.setGeometry(QtCore.QRect(290, 220, 131, 31))
        self.signUpSubmit.setObjectName(_fromUtf8("signUpSubmit"))
        self.twitter = QtGui.QPushButton(self.frame)
        self.twitter.setGeometry(QtCore.QRect(30, 200, 111, 101))
        self.twitter.setStyleSheet(_fromUtf8("background-image: url(:/prefix/Pictures/Assets/Twitter.png);\n"
"background-color:transparent;\n"
"background-repeat: no-repeat;"))
        self.twitter.setText(_fromUtf8(""))
        self.twitter.setObjectName(_fromUtf8("twitter"))
        self.msg = QtGui.QLabel(self.frame)
        self.msg.setGeometry(QtCore.QRect(30, 310, 911, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.msg.setFont(font)
        self.msg.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);"))
        self.msg.setText(_fromUtf8(""))
        self.msg.setTextFormat(QtCore.Qt.RichText)
        self.msg.setWordWrap(True)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.msg.raise_()
        self.loginUsername.raise_()
        self.loginPassword.raise_()
        self.loginSubmit.raise_()
        self.signUpUsername.raise_()
        self.signUpPass.raise_()
        self.signUpEmail.raise_()
        self.signUpSubmit.raise_()
        self.twitter.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.loginUsername.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.loginPassword.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.loginSubmit.setText(_translate("MainWindow", "Login", None))
        self.signUpUsername.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.signUpPass.setPlaceholderText(_translate("MainWindow", "password", None))
        self.signUpEmail.setPlaceholderText(_translate("MainWindow", "Email", None))
        self.signUpSubmit.setText(_translate("MainWindow", "Sign Up", None))

import rs1

if __name__ == "__main__":
    import sys
    import os
    from pymongo import MongoClient
    #import twitter
    client = MongoClient()

    usersDB = client['vocabulary-builder']
    users = usersDB['users']
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    def createUser(username, name, userType, secret):

        """
        Creates new user if username is not already taken
        """
        if users.posts.find_one({'username' : username}):
            ui.msg.setText("Sorry! This username has already been taken")
            newUser = None
        else:
            user = {'username' : username,
                    'name' : name,
                    'userType' : userType,
                    'secret' : secret
            }
            newUser = users.posts.insert_one(user)
            ui.msg.setText("User " + str(username) + " successfully created!")

    def signUpSubmit():
        uName = str(ui.signUpUsername.text())
        pwd = str(ui.signUpPass.text())
        fName = str(ui.signUpEmail.text())
        createUser(uName, fName, 'Normal', pwd)

    def verifyUser(username, pwd):
        """
        Verifies the user.
        Prints whether the user exists or not
        """
        if users.posts.find_one({'username' : username}):
            if users.posts.find_one({'secret' : pwd}):
                ui.msg.setText("successfull login plz do something")
                os.system("python landing.py "+username)
                sys.exit()
                
            else:
                ui.msg.setText("Invalid Password")
        else:
            ui.msg.setText("Invalid Username")
    def loginSubmit():
        uName = str(ui.loginUsername.text())
        pwd = str(ui.loginPassword.text())        
        verifyUser(uName, pwd)

    ui.signUpSubmit.clicked.connect(signUpSubmit)
    ui.loginSubmit.clicked.connect(loginSubmit)


    MainWindow.show()
    sys.exit(app.exec_())

