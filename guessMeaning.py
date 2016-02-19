import random

WORDLIST_FILENAME = "wordsMean.txt"

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



wordsDB = loadWords()


def chooseWord(wordsRDD, numChoose = 1):
    # wordsRDD (RDD): RDD of words and data (strings)
    secretWord = []
    wordList = wordsRDD
    #wordList = wordsRDD.collect()
    for num in range(numChoose):
        word = random.choice(wordList)
        secretWord.append(word)
        wordList.remove(word)
    return secretWord


def guessMeaning(fourWords):
    '''
    wordsDB: RDD, data of 4 words.

    Starts up an interactive module of guessing correct meaning.

    * At the start of the game, let the user know the secret word.

    * Ask the user to supply one guess (i.e. number).

    * The user should receive feedback immediately after guess
      about whether their guessed meaning is the actual meaning.
    '''
    correctMeaning = fourWords[0][1]
    print "Welcome to the guess meaning module!"
    print "Which of the following meanings are closest to the word: " + fourWords[0][0] + "?"
    print "Points assigned: " + fourWords[0][3]
    print "Difficulty: " + fourWords[0][4]
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
    
    
secretWord = chooseWord(wordsDB, 4)
guessMeaning(secretWord)