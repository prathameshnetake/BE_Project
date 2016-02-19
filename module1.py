# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module1.ui'
#
# Created: Fri Nov 13 23:19:52 2015
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
        MainWindow.resize(1319, 894)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"    background-image: url(:/prefix/Pictures/back1.jpg);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(80, 10, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.guessleft_label = QtGui.QLabel(self.centralwidget)
        self.guessleft_label.setGeometry(QtCore.QRect(90, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.guessleft_label.setFont(font)
        self.guessleft_label.setObjectName(_fromUtf8("guessleft_label"))
        self.score_label = QtGui.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(960, 50, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.score_label.setFont(font)
        self.score_label.setObjectName(_fromUtf8("score_label"))
        self.score = QtGui.QLCDNumber(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(1100, 50, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setFrameShape(QtGui.QFrame.NoFrame)
        self.score.setFrameShadow(QtGui.QFrame.Sunken)
        self.score.setProperty("value", 0.0)
        self.score.setObjectName(_fromUtf8("score"))
        self.guessLeft = QtGui.QLCDNumber(self.centralwidget)
        self.guessLeft.setGeometry(QtCore.QRect(270, 100, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.meaning_label = QtGui.QLabel(self.centralwidget)
        self.meaning_label.setGeometry(QtCore.QRect(90, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.meaning_label.setFont(font)
        self.meaning_label.setObjectName(_fromUtf8("meaning_label"))
        self.meaning = QtGui.QLabel(self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(230, 160, 811, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.meaning.setFont(font)
        self.meaning.setText(_fromUtf8(""))
        self.meaning.setObjectName(_fromUtf8("meaning"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 240, 1121, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.word = QtGui.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(80, 290, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setText(_fromUtf8(""))
        self.word.setObjectName(_fromUtf8("word"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.length = QtGui.QLCDNumber(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(270, 200, 71, 51))
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
        self.input = QtGui.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(90, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.input.setFont(font)
        self.input.setObjectName(_fromUtf8("input"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(200, 360, 111, 41))
        self.submit.setObjectName(_fromUtf8("submit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.title.setText(_translate("MainWindow", "Guess Word", None))
        self.guessleft_label.setText(_translate("MainWindow", "Guesses Left", None))
        self.score_label.setText(_translate("MainWindow", "Score", None))
        self.meaning_label.setText(_translate("MainWindow", "Meaning", None))
        self.label_4.setText(_translate("MainWindow", "Word Length", None))
        self.submit.setText(_translate("MainWindow", "Submit", None))

import rs1
import string
import random

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
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


    
    def isWordGuessed(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: boolean, True if all the letters of secretWord are in lettersGuessed;
          False otherwise
        '''
        # FILL IN YOUR CODE HERE...
        for i in secretWord:
            if i not in lettersGuessed:
                return False
     
        return True


    def getAvailableLetters(lettersGuessed):
        '''
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters that represents what letters have not
          yet been guessed.
        '''
        # FILL IN YOUR CODE HERE...
        availableLetters=""
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in lettersGuessed:
                availableLetters += i
     
        return availableLetters


    def getGuessedWord(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters and underscores that represents
          what letters in secretWord have been guessed so far.
        '''
        # FILL IN YOUR CODE HERE...
        guessedWord = ""
        for i in secretWord:
            if i in lettersGuessed:
                guessedWord += i
            else:
                guessedWord += " _ "
     
        return guessedWord
     
    guessedLetters = ""
    def hangman(secretWord):
        wordLen = len(secretWord)      
        
        ui.guessLeft.setProperty("value", float(8))
        def clicked():
            numGuesses = ui.guessLeft.value()
            global guessedLetters
            guess = ""
            if numGuesses > 0:
                availableLetters = getAvailableLetters(guessedLetters)
                if isWordGuessed(secretWord, guessedLetters):
                    w.last.setText("Congratulations, you won!")
                    #break
                guess = str(ui.input.text())

                guess = guess.lower()
                if guess not in availableLetters:
                    ui.word.setText("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessedLetters))
                elif guess in secretWord:
                    guessedLetters = guessedLetters + guess
                    ui.word.setText("Good Guess: " + getGuessedWord(secretWord, guessedLetters))
                    ui.input.setText("")
                else:
                    guessedLetters = guessedLetters + guess
                    ui.word.setText("Oops! That letter is not in my word: " + getGuessedWord(secretWord, guessedLetters))
                    ui.guessLeft.setProperty("value", float(ui.guessLeft.value()-1))
                    ui.input.setText("")


            print "Prathamesh"+guess
        


        ui.length.setProperty("value", float(wordLen))
        ui.submit.clicked.connect(clicked)
        




    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    ui.meaning.setText(secretWord)

























    sys.exit(app.exec_())

