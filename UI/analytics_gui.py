# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analytics.ui'
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet(_fromUtf8("QFrame{\n"
"\n"
"    background-image: url(:/prefix/Pictures/Assets/analytics.jpg);\n"
"}\n"
"QGroupBox{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 63 24pt \"Ubuntu\";\n"
"}\n"
"QPushButton{\n"
"    font: 12pt \"Yu Gothic UI\";\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1001, 701))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pichart = QtGui.QGroupBox(self.frame)
        self.pichart.setGeometry(QtCore.QRect(510, 460, 231, 221))
        self.pichart.setStyleSheet(_fromUtf8(""))
        self.pichart.setObjectName(_fromUtf8("pichart"))
        self.piTotal = QtGui.QPushButton(self.pichart)
        self.piTotal.setGeometry(QtCore.QRect(20, 70, 201, 41))
        self.piTotal.setObjectName(_fromUtf8("piTotal"))
        self.piCorrect = QtGui.QPushButton(self.pichart)
        self.piCorrect.setGeometry(QtCore.QRect(20, 120, 201, 41))
        self.piCorrect.setObjectName(_fromUtf8("piCorrect"))
        self.piWrong = QtGui.QPushButton(self.pichart)
        self.piWrong.setGeometry(QtCore.QRect(20, 170, 201, 41))
        self.piWrong.setObjectName(_fromUtf8("piWrong"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(750, 460, 231, 221))
        self.groupBox_2.setStyleSheet(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cloudTotal = QtGui.QPushButton(self.groupBox_2)
        self.cloudTotal.setGeometry(QtCore.QRect(20, 70, 201, 41))
        self.cloudTotal.setObjectName(_fromUtf8("cloudTotal"))
        self.cloudCorrect = QtGui.QPushButton(self.groupBox_2)
        self.cloudCorrect.setGeometry(QtCore.QRect(20, 120, 201, 41))
        self.cloudCorrect.setObjectName(_fromUtf8("cloudCorrect"))
        self.cloudWrong = QtGui.QPushButton(self.groupBox_2)
        self.cloudWrong.setGeometry(QtCore.QRect(20, 170, 201, 41))
        self.cloudWrong.setObjectName(_fromUtf8("cloudWrong"))
        self.histogram = QtGui.QPushButton(self.frame)
        self.histogram.setGeometry(QtCore.QRect(290, 640, 201, 41))
        self.histogram.setObjectName(_fromUtf8("histogram"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Analytics", None))
        self.pichart.setTitle(_translate("MainWindow", "Pi Charts", None))
        self.piTotal.setText(_translate("MainWindow", "Total", None))
        self.piCorrect.setText(_translate("MainWindow", "Correct", None))
        self.piWrong.setText(_translate("MainWindow", "Wrong", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Word Cloud", None))
        self.cloudTotal.setText(_translate("MainWindow", "Total", None))
        self.cloudCorrect.setText(_translate("MainWindow", "Correct", None))
        self.cloudWrong.setText(_translate("MainWindow", "Wrong", None))
        self.histogram.setText(_translate("MainWindow", "Histogram", None))

import rs1

if __name__ == "__main__":
    import sys
    import Analytics

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    def pi_Total():
        print "inside piTotal"
        Analytics.pieChart(username, 'total')


    ui.piTotal.clicked.connect(pi_Total)
    ui.cloudTotal.clicked.connect(pi_Total)
    MainWindow.show()
    sys.exit(app.exec_())

