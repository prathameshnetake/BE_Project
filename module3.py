# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module3.ui'
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
        MainWindow.resize(1067, 700)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.score_label = QtGui.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(620, 20, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.score_label.setFont(font)
        self.score_label.setObjectName(_fromUtf8("score_label"))
        self.score = QtGui.QLCDNumber(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(770, 20, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setFrameShape(QtGui.QFrame.NoFrame)
        self.score.setFrameShadow(QtGui.QFrame.Sunken)
        self.score.setProperty("value", 0.0)
        self.score.setObjectName(_fromUtf8("score"))
        self.length = QtGui.QLCDNumber(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(270, 160, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.length.setFont(font)
        self.length.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.length.setFrameShape(QtGui.QFrame.NoFrame)
        self.length.setFrameShadow(QtGui.QFrame.Sunken)
        self.length.setSmallDecimalPoint(False)
        self.length.setMode(QtGui.QLCDNumber.Dec)
        self.length.setProperty("value", 0.0)
        self.length.setObjectName(_fromUtf8("length"))
        self.guessleft_label = QtGui.QLabel(self.centralwidget)
        self.guessleft_label.setGeometry(QtCore.QRect(30, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.guessleft_label.setFont(font)
        self.guessleft_label.setAlignment(QtCore.Qt.AlignCenter)
        self.guessleft_label.setObjectName(_fromUtf8("guessleft_label"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.points = QtGui.QLCDNumber(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(490, 160, 131, 71))
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
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 240, 1011, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.guessLeft = QtGui.QLCDNumber(self.centralwidget)
        self.guessLeft.setGeometry(QtCore.QRect(30, 160, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.guessLeft.setFont(font)
        self.guessLeft.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.guessLeft.setFrameShape(QtGui.QFrame.NoFrame)
        self.guessLeft.setFrameShadow(QtGui.QFrame.Sunken)
        self.guessLeft.setSmallDecimalPoint(False)
        self.guessLeft.setMode(QtGui.QLCDNumber.Dec)
        self.guessLeft.setProperty("value", 0.0)
        self.guessLeft.setObjectName(_fromUtf8("guessLeft"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.difficulty = QtGui.QLCDNumber(self.centralwidget)
        self.difficulty.setGeometry(QtCore.QRect(700, 160, 131, 71))
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
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 20, 451, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Handwriting"))
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.input = QtGui.QLineEdit(self.centralwidget)
        self.input.setEnabled(True)
        self.input.setGeometry(QtCore.QRect(50, 460, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.input.setFont(font)
        self.input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.input.setObjectName(_fromUtf8("input"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(50, 520, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.submit.setFont(font)
        self.submit.setObjectName(_fromUtf8("submit"))
        self.msg = QtGui.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(50, 590, 911, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.msg.setFont(font)
        self.msg.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.msg.setText(_fromUtf8(""))
        self.msg.setTextFormat(QtCore.Qt.RichText)
        self.msg.setWordWrap(True)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.usWord = QtGui.QLabel(self.centralwidget)
        self.usWord.setGeometry(QtCore.QRect(50, 260, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.usWord.setFont(font)
        self.usWord.setObjectName(_fromUtf8("usWord"))
        self.usage = QtGui.QLabel(self.centralwidget)
        self.usage.setGeometry(QtCore.QRect(50, 350, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.usage.setFont(font)
        self.usage.setObjectName(_fromUtf8("usage"))
        self.orgin = QtGui.QLabel(self.centralwidget)
        self.orgin.setGeometry(QtCore.QRect(50, 400, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.orgin.setFont(font)
        self.orgin.setObjectName(_fromUtf8("orgin"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 1101, 741))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/prefix/Pictures/Assets/back4.jpg);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.msg.raise_()
        self.meaning = QtGui.QLabel(self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(50, 300, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.meaning.setFont(font)
        self.meaning.setObjectName(_fromUtf8("meaning"))
        self.frame.raise_()
        self.score_label.raise_()
        self.score.raise_()
        self.length.raise_()
        self.guessleft_label.raise_()
        self.label_5.raise_()
        self.points.raise_()
        self.label_6.raise_()
        self.line.raise_()
        self.guessLeft.raise_()
        self.label_4.raise_()
        self.difficulty.raise_()
        self.title.raise_()
        self.input.raise_()
        self.submit.raise_()
        self.msg.raise_()
        self.usWord.raise_()
        self.usage.raise_()
        self.orgin.raise_()
        self.meaning.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.score_label.setText(_translate("MainWindow", "Score", None))
        self.guessleft_label.setText(_translate("MainWindow", "Guesses Left", None))
        self.label_5.setText(_translate("MainWindow", "Points", None))
        self.label_6.setText(_translate("MainWindow", "Difficulty", None))
        self.label_4.setText(_translate("MainWindow", "Word Length", None))
        self.title.setText(_translate("MainWindow", "Use in sentence", None))
        self.submit.setText(_translate("MainWindow", "Submit", None))
        self.usWord.setText(_translate("MainWindow", "Use the following word in a sentence : ", None))
        self.usage.setText(_translate("MainWindow", "It is genrally used as : ", None))
        self.orgin.setText(_translate("MainWindow", "Origin of this word : ", None))
        self.meaning.setText(_translate("MainWindow", "Meaning : ", None))

import rs1
class moduleUIS:
    def __init__(self):     
        self.word = []
        self.wordToUse = None
        self.score = None
        self.wordlist = []
        self.meaning = None
        self.point = 0
        self.difficulty = 0
        self.usage = None
        self.origin = None


    def loadWords(self):
        import random       
        WORDLIST_FILENAME = "./final words DB"     
        inFile = open(WORDLIST_FILENAME, 'r', 0)        
        line = inFile.readline()
        wordlist = inFile.readlines()
        self.wordlist = wordlist

    def chooseWord (self):
        import random       
        self.word = random.choice(self.wordlist)
        
    def setup(self):
        import random
        temp = self.word.split('\t')
        self.wordToUse = temp[0]
        self.meaning = temp[1]
        self.usage = temp[2]        
        self.point = temp[3]
        self.difficulty = temp[4]
        self.origin = temp[5]
        
    def updateScore(self, score):
        f = open('./data/scores/module3.txt', 'r+')
        temp = f.readline()
        new = temp + score
        f.write(str(new))


    def fetchScore(self):
        f = open('./data/scores/module3.txt', 'r+')
        self.score = f.readline()


    def printall(self):
        print self.meaning
        print self.wordToUse

        print self.score
        print self.point



if __name__ == "__main__":
    import sys
    import time
    from gingerit.gingerit import GingerIt


    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    def playModule3():
        m = moduleUIS()
        m.loadWords()
        m.chooseWord()
        m.setup()
        m.fetchScore()
        m.printall()



        
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        ui.usWord.setText("Use the following word in a sentence : "+m.wordToUse)
        ui.usage.setText("It is genrally used as : "+m.usage)
        ui.orgin.setText("Origin of this word : "+m.origin)
        ui.points.setProperty("value", float(m.point))
        ui.difficulty.setProperty("value", float(m.difficulty))
        ui.score.setProperty("value", float(m.score))
        ui.meaning.setText("Meaning : "+m.meaning)

        def useInSentence():
            sentence = str(ui.input.text())
            if m.wordToUse not in sentence.split(' '):
                ui.msg.setText("You have not used %s in the sentence. Please check if the spelling and form used is correct!" % (m.wordToUse))
            else:
                parser = GingerIt()
                op = parser.parse(sentence)
                if not op['corrections']:
                    ui.msg.setText("Your sentence is correct!")
                else:
                    ui.msg.setText("The correct sentence should be: " + op['result'] + sentence[-1])
                app.processEvents()
                time.sleep(2)
                playModule3()


        ui.submit.clicked.connect(useInSentence)
    playModule3()
    MainWindow.show()
    sys.exit(app.exec_())
