# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcq.ui'
#
# Created: Fri Feb 19 23:18:31 2016
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
        MainWindow.resize(1173, 754)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(50, 640, 211, 51))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 1041, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.difficulty = QtGui.QLCDNumber(self.centralwidget)
        self.difficulty.setGeometry(QtCore.QRect(310, 190, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.difficulty.setFont(font)
        self.difficulty.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.difficulty.setFrameShape(QtGui.QFrame.NoFrame)
        self.difficulty.setFrameShadow(QtGui.QFrame.Sunken)
        self.difficulty.setSmallDecimalPoint(False)
        self.difficulty.setMode(QtGui.QLCDNumber.Dec)
        self.difficulty.setProperty("value", 0.0)
        self.difficulty.setObjectName(_fromUtf8("difficulty"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 270, 1171, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.points = QtGui.QLCDNumber(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(100, 200, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.points.setFont(font)
        self.points.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.points.setFrameShape(QtGui.QFrame.NoFrame)
        self.points.setFrameShadow(QtGui.QFrame.Sunken)
        self.points.setSmallDecimalPoint(False)
        self.points.setMode(QtGui.QLCDNumber.Dec)
        self.points.setProperty("value", 0.0)
        self.points.setObjectName(_fromUtf8("points"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.score_label = QtGui.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(790, 30, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.score_label.setFont(font)
        self.score_label.setObjectName(_fromUtf8("score_label"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 30, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.score = QtGui.QLCDNumber(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(950, 20, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setFrameShape(QtGui.QFrame.NoFrame)
        self.score.setFrameShadow(QtGui.QFrame.Sunken)
        self.score.setProperty("value", 0.0)
        self.score.setObjectName(_fromUtf8("score"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 370, 1101, 251))
        self.frame.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"font: 13pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: #808080;\n"
"border-radius: 10px;\n"
"text-align: left;\n"
"\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.option1 = QtGui.QPushButton(self.frame)
        self.option1.setGeometry(QtCore.QRect(0, 16, 1091, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.option1.setFont(font)
        self.option1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option1.setObjectName(_fromUtf8("option1"))
        self.option2 = QtGui.QPushButton(self.frame)
        self.option2.setGeometry(QtCore.QRect(0, 70, 1091, 41))
        self.option2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option2.setObjectName(_fromUtf8("option2"))
        self.option3 = QtGui.QPushButton(self.frame)
        self.option3.setGeometry(QtCore.QRect(0, 130, 1091, 41))
        self.option3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option3.setObjectName(_fromUtf8("option3"))
        self.option4 = QtGui.QPushButton(self.frame)
        self.option4.setGeometry(QtCore.QRect(0, 190, 1091, 41))
        self.option4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option4.setObjectName(_fromUtf8("option4"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.submit.setText(_translate("MainWindow", "Submit", None))
        self.label_5.setText(_translate("MainWindow", "Which of the following meanings are closest to the word:", None))
        self.label_6.setText(_translate("MainWindow", "Points", None))
        self.label_8.setText(_translate("MainWindow", "Difficulty", None))
        self.score_label.setText(_translate("MainWindow", "Score", None))
        self.title.setText(_translate("MainWindow", "Chooose Meaning", None))
        self.option1.setText(_translate("MainWindow", "PushButton", None))
        self.option2.setText(_translate("MainWindow", "PushButton", None))
        self.option3.setText(_translate("MainWindow", "PushButton", None))
        self.option4.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

