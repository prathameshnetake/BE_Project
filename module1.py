# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module1.ui'
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
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet(_fromUtf8("QMainWindow{\n"
"    \n"
"    background-image: url(:/prefix/Pictures/Assets/back2.jpg);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 30, 461, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Handwriting"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.guessleft_label = QtGui.QLabel(self.centralwidget)
        self.guessleft_label.setGeometry(QtCore.QRect(90, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.guessleft_label.setFont(font)
        self.guessleft_label.setAlignment(QtCore.Qt.AlignCenter)
        self.guessleft_label.setObjectName(_fromUtf8("guessleft_label"))
        self.score_label = QtGui.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(660, 20, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.score_label.setFont(font)
        self.score_label.setObjectName(_fromUtf8("score_label"))
        self.score = QtGui.QLCDNumber(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(830, 20, 141, 71))
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
        self.guessLeft.setGeometry(QtCore.QRect(100, 160, 141, 71))
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
        self.meaning_label = QtGui.QLabel(self.centralwidget)
        self.meaning_label.setGeometry(QtCore.QRect(90, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.meaning_label.setFont(font)
        self.meaning_label.setObjectName(_fromUtf8("meaning_label"))
        self.meaning = QtGui.QLabel(self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(210, 240, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.meaning.setFont(font)
        self.meaning.setText(_fromUtf8(""))
        self.meaning.setObjectName(_fromUtf8("meaning"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 220, 1121, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.msg = QtGui.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(70, 570, 881, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.msg.setFont(font)
        self.msg.setText(_fromUtf8(""))
        self.msg.setObjectName(_fromUtf8("msg"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.length = QtGui.QLCDNumber(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(310, 160, 131, 71))
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
        self.input.setEnabled(True)
        self.input.setGeometry(QtCore.QRect(70, 510, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.input.setFont(font)
        self.input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.input.setObjectName(_fromUtf8("input"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(180, 510, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.submit.setFont(font)
        self.submit.setObjectName(_fromUtf8("submit"))
        self.word = QtGui.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(350, 460, 621, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setText(_fromUtf8(""))
        self.word.setObjectName(_fromUtf8("word"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 110, 171, 31))
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
        self.points.setGeometry(QtCore.QRect(510, 160, 131, 71))
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
        self.difficulty = QtGui.QLCDNumber(self.centralwidget)
        self.difficulty.setGeometry(QtCore.QRect(720, 150, 131, 71))
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
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.meaning_label_2 = QtGui.QLabel(self.centralwidget)
        self.meaning_label_2.setGeometry(QtCore.QRect(90, 310, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.meaning_label_2.setFont(font)
        self.meaning_label_2.setObjectName(_fromUtf8("meaning_label_2"))
        self.usage = QtGui.QLabel(self.centralwidget)
        self.usage.setGeometry(QtCore.QRect(210, 310, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.usage.setFont(font)
        self.usage.setText(_fromUtf8(""))
        self.usage.setObjectName(_fromUtf8("usage"))
        self.meaning_label_3 = QtGui.QLabel(self.centralwidget)
        self.meaning_label_3.setGeometry(QtCore.QRect(90, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.meaning_label_3.setFont(font)
        self.meaning_label_3.setObjectName(_fromUtf8("meaning_label_3"))
        self.origin = QtGui.QLabel(self.centralwidget)
        self.origin.setGeometry(QtCore.QRect(220, 370, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.origin.setFont(font)
        self.origin.setText(_fromUtf8(""))
        self.origin.setObjectName(_fromUtf8("origin"))
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(880, 650, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit.setFont(font)
        self.exit.setObjectName(_fromUtf8("exit"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Module 1", None))
        self.title.setText(_translate("MainWindow", "Guess Word", None))
        self.guessleft_label.setText(_translate("MainWindow", "Guesses Left", None))
        self.score_label.setText(_translate("MainWindow", "Score", None))
        self.meaning_label.setText(_translate("MainWindow", "Meaning", None))
        self.label_4.setText(_translate("MainWindow", "Word Length", None))
        self.submit.setText(_translate("MainWindow", "Submit", None))
        self.label_5.setText(_translate("MainWindow", "Points", None))
        self.label_6.setText(_translate("MainWindow", "Difficulty", None))
        self.meaning_label_2.setText(_translate("MainWindow", "Usage", None))
        self.meaning_label_3.setText(_translate("MainWindow", "Origin", None))
        self.exit.setText(_translate("MainWindow", "Exit", None))

import rs1
import random 
import string
if __name__ == "__main__":
    import sys
    import usersMongo
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    WORDLIST_FILENAME = "./Final Words DB"
    username = sys.argv[1]



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
        wordlist = inFile.readlines()
        #print l
        # wordlist: list of strings
        #wordlist = string.split(line)
        
        print "  ", len(wordlist), "words loaded."
        return wordlist

    def chooseLine(wordlist):
        '''
        wordlist is list of all lines
        '''
        
        return random.choice(wordlist)

    def chooseWord(wordlist):
        """
        wordlist (list): list of words (strings)

        Returns a word from wordlist at random
        """
        line = chooseLine(wordlist)
        lineList = line.split('\t')
        print lineList        
        return lineList[0], lineList[1], lineList[2], lineList[3], lineList[4][0:2] , lineList[5]   
    
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

    def updateWord():
        ui.word.setText(str(getGuessedWord(secretWord, guessedLetters)))
        ui.input.setFocus()

    wordlist = loadWords()
    secretWord, meaning, usage, points, difficulty, origin = chooseWord(wordlist) 





    def hangman(secretWord):
        wordLen = len(secretWord)      
        updateWord()
        ui.guessLeft.setProperty("value", float(8))
        def clicked():
            numGuesses = ui.guessLeft.value()
            global guessedLetters
            guess = ""
            if numGuesses > 0:
                availableLetters = getAvailableLetters(guessedLetters)
                if isWordGuessed(secretWord, guessedLetters):
                    ui.msg.setText("Congratulations, you won!")
                    usersMongo.updateAttempts(username, secretWord, 1)
                    
                    #break
                guess = str(ui.input.text())

                guess = guess.lower()
                if guess not in availableLetters:
                    ui.msg.setText("Oops! You've already guessed that letter")
                    updateWord()
                    ui.input.setText("")
                elif guess in secretWord:
                    guessedLetters = guessedLetters + guess
                    ui.msg.setText("Good Guess: ")
                    updateWord()
                    ui.input.setText("")
                else:
                    guessedLetters = guessedLetters + guess
                    ui.msg.setText("Oops! That letter is not in my word: ")
                    updateWord()
                    ui.guessLeft.setProperty("value", float(ui.guessLeft.value()-1))
                    ui.input.setText("")
            if numGuesses == 0:
                ui.msg.setText("Sorry! You loose "+secretWord+" was the word")
                usersMongo.updateAttempts(username, secretWord, -1)
                
            print "Prathamesh"+guess
        ui.length.setProperty("value", float(wordLen))
        ui.submit.clicked.connect(clicked)
        
    def close():
        sys.exit()


    
    
    print secretWord  
    hangman(secretWord)
    ui.meaning.setText(meaning)
    ui.usage.setText(usage)
    ui.points.setProperty("value", float(points))
    ui.difficulty.setProperty("value", float(difficulty))
    ui.origin.setText(origin)
    ui.exit.clicked.connect(close)

    



    sys.exit(app.exec_())