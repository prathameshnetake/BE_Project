# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcq.ui'
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
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1005, 696)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet(_fromUtf8("QFrame#all_frame{\n"
"\n"
"    background-image: url(:/prefix/Pictures/Assets/back4.jpg);\n"
"\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(50, 640, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.submit.setFont(font)
        self.submit.setObjectName(_fromUtf8("submit"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 1041, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.difficulty = QtGui.QLCDNumber(self.centralwidget)
        self.difficulty.setGeometry(QtCore.QRect(280, 190, 131, 71))
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
        self.line.setGeometry(QtCore.QRect(0, 270, 1011, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 150, 171, 31))
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
        self.points.setGeometry(QtCore.QRect(70, 200, 131, 71))
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
        self.label_8.setGeometry(QtCore.QRect(280, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.score_label = QtGui.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(640, 30, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.score_label.setFont(font)
        self.score_label.setObjectName(_fromUtf8("score_label"))
        self.score = QtGui.QLCDNumber(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(800, 40, 171, 71))
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
"font: 10pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: #808080;\n"
"border-radius: 10px;\n"
"text-align: left;\n"
"\n"
"}\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.option1 = QtGui.QPushButton(self.frame)
        self.option1.setEnabled(True)
        self.option1.setGeometry(QtCore.QRect(0, 16, 921, 41))
        self.option1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option1.setObjectName(_fromUtf8("option1"))
        self.option2 = QtGui.QPushButton(self.frame)
        self.option2.setGeometry(QtCore.QRect(0, 70, 921, 41))
        self.option2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option2.setObjectName(_fromUtf8("option2"))
        self.option3 = QtGui.QPushButton(self.frame)
        self.option3.setGeometry(QtCore.QRect(0, 130, 921, 41))
        self.option3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option3.setObjectName(_fromUtf8("option3"))
        self.option4 = QtGui.QPushButton(self.frame)
        self.option4.setGeometry(QtCore.QRect(0, 190, 921, 41))
        self.option4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.option4.setObjectName(_fromUtf8("option4"))
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(860, 650, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit.setFont(font)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.all_frame = QtGui.QFrame(self.centralwidget)
        self.all_frame.setGeometry(QtCore.QRect(-20, -10, 1041, 721))
        self.all_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.all_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.all_frame.setObjectName(_fromUtf8("all_frame"))
        self.title = QtGui.QLabel(self.all_frame)
        self.title.setGeometry(QtCore.QRect(40, 40, 521, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Handwriting"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.all_frame.raise_()
        self.submit.raise_()
        self.label_5.raise_()
        self.difficulty.raise_()
        self.line.raise_()
        self.label_6.raise_()
        self.points.raise_()
        self.label_8.raise_()
        self.score_label.raise_()
        self.score.raise_()
        self.frame.raise_()
        self.exit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Module 2", None))
        self.submit.setText(_translate("MainWindow", "Submit", None))
        self.label_5.setText(_translate("MainWindow", "Which of the following meanings are closest to the word:", None))
        self.label_6.setText(_translate("MainWindow", "Points", None))
        self.label_8.setText(_translate("MainWindow", "Difficulty", None))
        self.score_label.setText(_translate("MainWindow", "Score", None))
        self.option1.setText(_translate("MainWindow", "PushButton", None))
        self.option2.setText(_translate("MainWindow", "PushButton", None))
        self.option3.setText(_translate("MainWindow", "PushButton", None))
        self.option4.setText(_translate("MainWindow", "PushButton", None))
        self.exit.setText(_translate("MainWindow", "Exit", None))
        self.title.setText(_translate("MainWindow", "Chooose Meaning", None))

import rs1

class option(object):
    """This class will take control for the selection made by the user"""


    def __init__(self):
        
        self.choice = None

    def select1(self):
        self.choice = 1
        print 'Now selection is 1'

    def select2(self):
        print 'Now selection is 2'
        self.choice = 2

    def select3(self):
        print 'Now selection is 3'
        self.choice = 3

    def select4(self):
        print 'Now selection is 4'
        self.choice = 4
    def getChoice(self):
        return self.choice
        

class MeaningMCQ:   
    def __init__(self):     
        self.fourWords = []
        self.score = 20
        self.wordlist = []
        self.correctMeaning = None
        self.point = 0
        self.difficulty = 0
        self.wordToGuess = None
        self.options = []
        
    def loadWords(self):
        import random       
        WORDLIST_FILENAME = "./Final Words DB"     
        inFile = open(WORDLIST_FILENAME, 'r', 0)        
        line = inFile.readline()
        wordlist = inFile.readlines()
        self.wordlist = wordlist

    def chooseFourWords(self):
        import random
        secretWord = []
        for i in range(4):
            word = random.choice(self.wordlist)
            secretWord.append(word.split('\t'))
            self.wordlist.remove(word)
        self.fourWords = secretWord     

    def setup(self):
        import random
        self.correctMeaning = self.fourWords[0][1]
        self.wordToGuess = self.fourWords[0][0]
        self.point = self.fourWords[0][3]
        self.difficulty = self.fourWords[0][4]
        random.shuffle(self.fourWords)
        for j in range(4):
            self.options.append(self.fourWords[j][1])
        print self.correctMeaning
    def printall(self):
        print self.wordToGuess
        print self.fourWords
        print self.options




       

if __name__ == "__main__":
    import sys
    import random
    import time
    import usersMongo

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    username = sys.argv[1]


    def playModule2():
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        #object for selection
        sel = option()

        #object for genrating the word

        start = MeaningMCQ()
        start.loadWords()
        start.chooseFourWords()
        start.setup()
        #Now setting up UI

        ui.option1.setText("  1. "+str(start.options[0]))
        ui.option2.setText("  2. "+str(start.options[1]))
        ui.option3.setText("  3. "+str(start.options[2]))
        ui.option4.setText("  4. "+str(start.options[3]))



        ui.label_5.setText("Which of the following meanings are closest to the word :- "+str(start.wordToGuess)+" ?")
        ui.option1.clicked.connect(sel.select1)
        ui.option2.clicked.connect(sel.select2)
        ui.option3.clicked.connect(sel.select3)
        ui.option4.clicked.connect(sel.select4)
        ui.points.setProperty("value", float(start.point))
        ui.difficulty.setProperty("value", float(start.difficulty[:2]))

        #processing the option buttons
        def close():
            sys.exit()

        def process():
            final = sel.getChoice()
            print "The fianl choice is ",final
            ui.option1.setEnabled(False)
            ui.option2.setEnabled(False)
            ui.option3.setEnabled(False)
            ui.option4.setEnabled(False)
            if start.fourWords[final -1][1] == start.correctMeaning:
                print 'That is correct sending data to ML'
                usersMongo.updateAttempts(username, start.wordToGuess, 1)
                print final
                if final == 1:
                    ui.option1.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
                elif final == 2:
                    ui.option2.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
                elif final == 3:
                    ui.option3.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
                else:
                    ui.option4.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
            else:
                print 'That is wrong sending data to ML'
                usersMongo.updateAttempts(username, start.wordToGuess, -1)
                print final
                if final == 1:
                    ui.option1.setStyleSheet(_fromUtf8("background-color: #cc3300;\n"))
                elif final == 2:
                    ui.option2.setStyleSheet(_fromUtf8("background-color: #cc3300;\n"))
                elif final == 3:
                    ui.option3.setStyleSheet(_fromUtf8("background-color: #cc3300;\n"))
                else:
                    ui.option4.setStyleSheet(_fromUtf8("background-color: #cc3300;\n"))
                for i in range(4):
                    if start.fourWords[i][1] == start.correctMeaning:
                        if i == 0:
                            ui.option1.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
                        elif i == 1:
                            ui.option2.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
                        elif i == 2:
                            ui.option3.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
                        else:
                            ui.option4.setStyleSheet(_fromUtf8("background-color: #33cc33;\n"))
            app.processEvents()
            time.sleep(2)
            playModule2()

        


        ui.submit.clicked.connect(process)
        ui.exit.clicked.connect(close)
    playModule2()
    MainWindow.show()
    sys.exit(app.exec_())
