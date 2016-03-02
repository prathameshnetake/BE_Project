# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import random
import string
from gingerit.gingerit import GingerIt

# <codecell>

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    home = os.environ.get('HOME', None)
    inFile = sc.textFile(home + "/Documents/spark-1.4.1-bin-hadoop2.6/Final Words DB")
    # wordsRDD: RDD
    wordsRDD = (inFile
            .map(lambda wordData: wordData.split('\t'))
            .map(lambda wordData: map(str, wordData))
            .cache())
    wordsCount = wordsRDD.count()
    print "  ", wordsCount, "words loaded."
    return wordsRDD

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordsDB = loadWords()

# <codecell>

def chooseWord(wordsRDD, numChoose = 1):
    # wordsRDD (RDD): RDD of words and data (strings)
    wordList = wordsRDD.collect()
    if numChoose == 1:
        return random.choice(wordList)
    else:
        fourWords = []
        for num in range(numChoose):
            word = random.choice(wordList)
            fourWords.append(word)
            wordList.remove(word)
        return fourWords

# <codecell>

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret=[]
   
    for letters in secretWord:
        while letters not in secret:
            secret.append(letters)

    for char in lettersGuessed:
        if char in secret:
            secret.remove(char)

    if secret == []:
        return True
    else:
        return False

# <codecell>

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secret = []
    index = 0
    temp = []
    ans = ''
    
    for s in secretWord:
        temp.append('_ ')
   
    for letters in secretWord:
        secret.append(letters)
    
    for char in lettersGuessed:
        while char in secret:
            index = secret.index(char)
            temp[index] = char
            secret.pop(index)
            secret.insert(index,'')

    for t in temp:
        ans += t
    return ans

# <codecell>

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    change = []
    ans = ''
    alpha = string.ascii_lowercase

    for char in alpha:
        change.append(char)

    for letters in lettersGuessed:
        if letters in change:
            change.remove(letters)

    for c in change:
        ans += c

    return ans

# <codecell>

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
    '''
    # 'exiguous', 'scanty; meager; small; slender', 'adjective', '19', '51-Few English speakers likely know this word', 'Late Latin'
    word = secretWord[0]
    meaning = secretWord[1]
    usage = secretWord[2]
    points = secretWord[3]
    difficulty = secretWord[4]
    origin = secretWord[5]
    mistakesMade = 0
    totalGuess = 8
    lettersGuessed = []
    rem = []
    inc = ''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(word)) + " letters long."
    print "The meaning of the word is: " + str(meaning)
    print "The usage of the word is: " + str(usage)
    print "Points assigned: " + str(points)
    print "Difficulty: " + str(difficulty)
    print "Origin: " + str(origin)
    print "-------------"
    while mistakesMade != 8:
        print "You have " + str(totalGuess) + " guesses left."
        print "Available letters: " + str(getAvailableLetters(lettersGuessed))
        inc = raw_input("Please guess a letter: ").lower()
        lettersGuessed.append(inc)
        if inc in rem:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord,lettersGuessed))
        elif inc in secretWord[0]:
            print "Good guess: " + str(getGuessedWord(secretWord[0],lettersGuessed))
        elif inc not in secretWord[0]:
            print "Oops! That letter is not in my word: " + str(getGuessedWord(secretWord[0],lettersGuessed))
            mistakesMade += 1
            totalGuess -= 1
        if isWordGuessed(secretWord[0],lettersGuessed):
            print "-------------"
            print "Congratulations, you won!"
            break
        print "-------------"
        rem.append(inc)
    if totalGuess == 0:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord[0])

# <codecell>

def guessMeaning(fourWords):
    '''
    fourWords: list, data of 4 words.

    Starts up an interactive module of guessing correct meaning.

    * At the start of the game, let the user know the secret word.

    * Ask the user to supply one guess (i.e. number).

    * The user should receive feedback immediately after guess
      about whether their guessed meaning is the actual meaning.
    '''
    # 'exiguous', 'scanty; meager; small; slender', 'adjective', '19', '51-Few English speakers likely know this word', 'Late Latin'
    correctMeaning = fourWords[0][1]
    print "Welcome to the guess meaning module!"
    print "Which of the following meanings are closest to the word: " + fourWords[0][0] + "?"
    print "Points assigned: " + fourWords[0][3]
    print "Difficulty: " + fourWords[0][4]
    print "Origin: " + fourWords[0][5]
    random.shuffle(fourWords)
    print
    print "1. " + fourWords[0][1]
    print "2. " + fourWords[1][1]
    print "3. " + fourWords[2][1]
    print "4. " + fourWords[3][1]
    print
    choice = int(raw_input("Enter number corresponding to the meaning which you seem fit: "))
    if fourWords[choice - 1][1] == correctMeaning:
        print "That is correct!"
    else:
        print "Oops! The correct meaning is: " + correctMeaning

# <codecell>

def useInSentence(secretWord):
    '''
    secretWor: list, word + data

    Starts up an interactive module of using word in sentence.

    * At the start of the game, let the user know the secret word.

    * Ask the user to supply one grammatically sentence containing the secret word.

    * The user should receive feedback immediately whether their sentence is correct.
    '''
    # 'exiguous', 'scanty; meager; small; slender', 'adjective', '19', '51-Few English speakers likely know this word', 'Late Latin'
    word = secretWord[0]
    meaning = secretWord[1]
    usage = secretWord[2]
    points = secretWord[3]
    difficulty = secretWord[4]
    origin = secretWord[5]
    print "Welcome to the use in a sentence module!"
    print "Use the following word in a sentence: " + word
    print "The meaning of " + word + " is: " + meaning
    print "It is generally used as (a/an): " + usage
    print "Points assigned: " + points
    print "Difficulty: " + difficulty
    print "Origin: " + origin
    
    sentence = raw_input("Sentence containing the above mentioned word: ")
    
    if word not in sentence.split(' '):
        print "You have not used %s in the sentence. Please check if the spelling and form used is correct!" % (word)
    else:
        parser = GingerIt()
        op = parser.parse(sentence)
        if not op['corrections']:
            print "Your sentence is correct!"
        else:
            print "The correct sentence should be: " + op['result'] + sentence[-1]

# <codecell>

secretWord = chooseWord(wordsDB)
hangman(secretWord)

# <codecell>

secretWord = chooseWord(wordsDB, 4)
guessMeaning(secretWord)

# <codecell>

secretWord = chooseWord(wordsDB)
useInSentence(secretWord)

# <codecell>


