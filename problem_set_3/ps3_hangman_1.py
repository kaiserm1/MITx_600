# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

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
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ""    
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return guessed_word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    available_letters = string.ascii_lowercase
    for letter in lettersGuessed:
        new_available_letters = ""
        available_letters = available_letters.split(letter)
        available_letters = new_available_letters.join(available_letters)
    return available_letters
    
def get_user_input(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    
    returns: string, comprised of ONE lower case letter from user input which
    is the current guess 
    '''
    print("- " * 13)
    print("You have " + str(guesses_left(lettersGuessed)) + " guesses left.")
    print(getAvailableLetters(lettersGuessed), end='')
    return(input("Please guess a letter: ").lower())
    
def guesses_left(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    
    returns: how many guesses are left (max = 8)
    '''
    return 8 - len(lettersGuessed)

def evaluate_user_input(a_string, secretWord, lettersGuessed):
    '''
    a_string: single lower case letter from user input
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    
    returns: if guess was correct, returns guess, 
             if guess was used already, return "oh shucks, input again", 
             if guess is wrong, return "wrong guess"
    '''
    if a_string in lettersGuessed:
        answer = "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        return (answer, lettersGuessed)
    elif a_string in secretWord:
        lettersGuessed.append(a_string)
        answer = "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        return (answer, lettersGuessed)
    else:
        lettersGuessed.append(a_string)
        answer = "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
        return (answer, lettersGuessed)

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
    lettersGuessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word, that is " + str(len(secretWord)) + " letters long.")
    while guesses_left(lettersGuessed) > 0:
        guess = get_user_input(lettersGuessed)
        print(evaluate_user_input(guess, secretWord, lettersGuessed)[0])
        if isWordGuessed(secretWord, lettersGuessed):
            print("- " * 13)
            print("Congratulations, you won!")
            break
        elif guesses_left(lettersGuessed) == 0:
            print("- " * 13)
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        else:
            pass




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = "martin"
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

