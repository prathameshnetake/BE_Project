# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(609, 499)
        Form.setStyleSheet(_fromUtf8("background-color: #462148;\n"
""))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(110, 130, 401, 301))
        self.frame.setStyleSheet(_fromUtf8("QFrame{\n"
"    background-color: #f2f2f2;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton{\n"
"    background-color: #704c73;\n"
"    color: #eae7ea;\n"
"    font: 12pt \"Segoe Print\";\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #b076b5;\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #3c283e\n"
"}\n"
"QTextEdit{\n"
"    font:16pt \"Verdana\";\n"
"    background-color: #f0eef0;\n"
"    border: 1px solid #e5e4e5;\n"
"}\n"
"QTextEdit:focus{    \n"
"    border: 3px solid #e5e4e5;\n"
"}\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.username = QtGui.QTextEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(30, 40, 351, 51))
        self.username.setStyleSheet(_fromUtf8(""))
        self.username.setFrameShadow(QtGui.QFrame.Raised)
        self.username.setLineWidth(1)
        self.username.setMidLineWidth(0)
        self.username.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.username.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.username.setTabChangesFocus(True)
        self.username.setAcceptRichText(False)
        self.username.setCursorWidth(4)
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QTextEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(30, 110, 351, 51))
        self.password.setStyleSheet(_fromUtf8(""))
        self.password.setFrameShadow(QtGui.QFrame.Raised)
        self.password.setLineWidth(1)
        self.password.setMidLineWidth(0)
        self.password.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.password.setTabChangesFocus(True)
        self.password.setAcceptRichText(False)
        self.password.setCursorWidth(4)
        self.password.setObjectName(_fromUtf8("password"))
        self.submit = QtGui.QPushButton(self.frame)
        self.submit.setGeometry(QtCore.QRect(130, 190, 171, 51))
        self.submit.setStyleSheet(_fromUtf8(""))
        self.submit.setObjectName(_fromUtf8("submit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "LoginForm", None))
        self.username.setToolTip(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Username</span></p></body></html>", None))
        self.username.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.password.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.submit.setText(_translate("Form", "Submit", None))

a = QtGui.QApplication(sys.argv)
w = Ui_Form()
w.show()
sys.exit(a.exec_())