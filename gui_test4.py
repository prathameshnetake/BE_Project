# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1088, 728)
        Form.setStyleSheet(_fromUtf8("QPushButton:: hover{\n"
"    background-color: #ffff;\n"
"}\n"
"\n"
""))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 650, 1311, 101))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(89, 89, 89);"))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 291, 651))
        self.frame_2.setStyleSheet(_fromUtf8("background-color: rgb(210, 241, 255);"))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 241, 31))
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 16pt \"Berlin Sans FB Demi\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(89, 89, 89); opacity: 0.5;\n"
"border-radius: 15px;\n"
"border: 1px solid white;\n"
"QPushButton:: hover{\n"
"background-color: rgb(187, 203, 255);}\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(290, 0, 1021, 651))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgb(176, 176, 176);"))
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(80, 40, 491, 91))
        self.label.setStyleSheet(_fromUtf8("font: 40pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);\n"
"text-border: 1px solid black;\n"
"\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 491, 61))
        self.label_2.setStyleSheet(_fromUtf8("font: 18pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.SecretWord = QtGui.QLabel(self.frame_3)
        self.SecretWord.setGeometry(QtCore.QRect(40, 250, 491, 61))
        self.SecretWord.setStyleSheet(_fromUtf8("font: 18pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);"))
        self.SecretWord.setObjectName(_fromUtf8("SecretWord"))
        self.available = QtGui.QLabel(self.frame_3)
        self.available.setGeometry(QtCore.QRect(40, 320, 491, 61))
        self.available.setStyleSheet(_fromUtf8("font: 18pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);"))
        self.available.setObjectName(_fromUtf8("available"))
        self.warning = QtGui.QLabel(self.frame_3)
        self.warning.setGeometry(QtCore.QRect(40, 460, 741, 61))
        self.warning.setStyleSheet(_fromUtf8("font: 18pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);"))
        self.warning.setText(_fromUtf8(""))
        self.warning.setObjectName(_fromUtf8("warning"))
        self.last = QtGui.QLabel(self.frame_3)
        self.last.setGeometry(QtCore.QRect(40, 520, 731, 61))
        self.last.setStyleSheet(_fromUtf8("font: 18pt \"Rockwell\";\n"
"color: rgb(255, 255, 255);"))
        self.last.setText(_fromUtf8(""))
        self.last.setObjectName(_fromUtf8("last"))
        self.input_text = QtGui.QLineEdit(self.frame_3)
        self.input_text.setGeometry(QtCore.QRect(40, 390, 101, 31))
        self.input_text.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.input_text.setPlaceholderText("Enter One charactor at a time..")
        self.input_text.setObjectName(_fromUtf8("input_text"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Guess Word ", None))
        self.label.setText(_translate("Form", "Vocablury Builder", None))
        self.label_2.setText(_translate("Form", "I am thinking of a letter that is 9 letter long", None))
        self.SecretWord.setText(_translate("Form", "-----------------", None))
        self.available.setText(_translate("Form", "Available Letters: ", None))


if __name__ == "__main__":
    import sys
    import random 
    import string
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    w = Ui_Form()
    w.setupUi(Form)




    Form.show()


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


    # Load the list of words into the variable wordlist
    # so that it can be accessed from anywhere in the program
    wordlist = loadWords()
     
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
         
     
    def hangman(secretWord):
        '''
        secretWord: string, the secret word to guess.
     
        Starts up an interactive game of Hangman.
     
        * At the start of the game, let the user know how many 
          letters the secretWord contains.
     
        * Ask the user to supply one guess (i.e. letter) per round.
     
        * The user should receive feedback immediately after each guess 
          about whether their guess appears in the computers word.
     
        * After each round, you should also display to the user the 
          partially guessed word so far, as well as letters that the 
          user has not yet guessed.
     
        Follows the other limitations detailed in the problem write-up.
        '''
        # FILL IN YOUR CODE HERE...
        wordLen = len(secretWord)
        numGuesses = 8
        guessedLetters = ""
        guess = ""         
        
        w.label_2.setText("I am thinking of a word that is " + str(wordLen) + " letters long")
         
        while numGuesses > 0:
            availableLetters = getAvailableLetters(guessedLetters)
            print "-------------"
            if isWordGuessed(secretWord, guessedLetters):
                w.last.setText("Congratulations, you won!")
                break
            w.SecretWord.setText("You have %d guesses left." % numGuesses)
            w.available.setText("Available letters: " + availableLetters)
            guess = raw_input("Please guess a letter: ")
            print str (w.input_text.text())
                      
                
            
            if len(guess) > 1:
                w.warning.setText("Please enter only one letter")
                continue
            guess = guess.lower()
            if guess not in availableLetters:
                w.warning.setText("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessedLetters))
            elif guess in secretWord:
                guessedLetters = guessedLetters + guess
                w.warning.setText("Good Guess: " + getGuessedWord(secretWord, guessedLetters))
            else:
                guessedLetters = guessedLetters + guess
                w.warning.setText("Oops! That letter is not in my word: " + getGuessedWord(secretWord, guessedLetters))
                numGuesses -= 1
     
        if numGuesses == 0:
            w.last.setText("Sorry, you ran out of guesses. The word was " + secretWord)
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    sys.exit(app.exec_())

