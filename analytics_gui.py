# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_analytics.ui'
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
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"    \n"
"    \n"
"    background-image: url(:/prefix/Pictures/Assets/analytics.jpg);\n"
"}\n"
"QGroupBox{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 63 24pt \"Ubuntu\";\n"
"}\n"
"QPushButton{\n"
"    color: rgb(0,0,0);\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 611, 71))
        self.label.setStyleSheet(_fromUtf8("font: 75 36pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(740, 340, 241, 341))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.module1 = QtGui.QPushButton(self.groupBox)
        self.module1.setGeometry(QtCore.QRect(20, 70, 201, 41))
        self.module1.setObjectName(_fromUtf8("module1"))
        self.module2 = QtGui.QPushButton(self.groupBox)
        self.module2.setGeometry(QtCore.QRect(20, 120, 201, 41))
        self.module2.setObjectName(_fromUtf8("module2"))
        self.module3 = QtGui.QPushButton(self.groupBox)
        self.module3.setGeometry(QtCore.QRect(20, 170, 201, 41))
        self.module3.setObjectName(_fromUtf8("module3"))
        self.logout = QtGui.QPushButton(self.groupBox)
        self.logout.setGeometry(QtCore.QRect(20, 290, 201, 41))
        self.logout.setObjectName(_fromUtf8("logout"))
        self.histogram = QtGui.QPushButton(self.groupBox)
        self.histogram.setGeometry(QtCore.QRect(20, 220, 201, 41))
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 340, 241, 341))
        self.groupBox_2.setStyleSheet(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.wordTotal = QtGui.QPushButton(self.groupBox_2)
        self.wordTotal.setGeometry(QtCore.QRect(20, 70, 201, 41))
        self.wordTotal.setObjectName(_fromUtf8("wordTotal"))
        self.wordCorrect = QtGui.QPushButton(self.groupBox_2)
        self.wordCorrect.setGeometry(QtCore.QRect(20, 120, 201, 41))
        self.wordCorrect.setObjectName(_fromUtf8("wordCorrect"))
        self.wordWrong = QtGui.QPushButton(self.groupBox_2)
        self.wordWrong.setGeometry(QtCore.QRect(20, 170, 201, 41))
        self.wordWrong.setObjectName(_fromUtf8("wordWrong"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Welcome User", None))
        self.groupBox.setTitle(_translate("MainWindow", "Pi  Charts", None))
        self.module1.setText(_translate("MainWindow", "Total", None))
        self.module2.setText(_translate("MainWindow", "Correct", None))
        self.module3.setText(_translate("MainWindow", "Wrong", None))
        self.logout.setText(_translate("MainWindow", "Logout", None))
        self.histogram.setText(_translate("MainWindow", "Histogram", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Word Cloud", None))
        self.wordTotal.setText(_translate("MainWindow", "Total", None))
        self.wordCorrect.setText(_translate("MainWindow", "Correct", None))
        self.wordWrong.setText(_translate("MainWindow", "Wrong", None))

import rs1

if __name__ == "__main__":
    import sys
    import os
    import Analytics
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    username = sys.argv[1]
    ui.label.setText("Welcome "+username)


    def module1():
        os.system("python module1.py "+username)

    def module2():
        os.system("python module2.py "+username)

    def module3():
        os.system("python module3.py "+username)

    def hist():
        os.system("python analytics_gui.py "+username)

    def word_total():
        os.system("python module1.py "+username)
    def logout():
        sys.exit()

    ui.module1.clicked.connect(module1)
    ui.module2.clicked.connect(module2)
    ui.module3.clicked.connect(module3)
    ui.histogram.clicked.connect(hist)
    ui.wordTotal.clicked.connect(word_total)
    ui.logout.clicked.connect(logout)

    MainWindow.show()
    sys.exit(app.exec_())