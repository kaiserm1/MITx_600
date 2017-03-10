# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

secretWord = 'apple'
lettersGuessed = ['a', 'p', 'l', 'e', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))