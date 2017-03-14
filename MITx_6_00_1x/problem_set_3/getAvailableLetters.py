# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for letter in lettersGuessed:
        new_available_letters = ""
        available_letters = available_letters.split(letter)
        available_letters = new_available_letters.join(available_letters)
    return available_letters