# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

        


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))