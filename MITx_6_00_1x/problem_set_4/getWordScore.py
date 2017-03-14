# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:30:16 2017

@author: maka_
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    assert type(word) == str, ('variable "word" not a string!')
    assert (type(n) == int and n > 0), ('variable "n" must be an int > 0')
    letter_values = []
    for letter in word:
        letter_values.append(SCRABBLE_LETTER_VALUES.get(letter))
    letter_values = sum(letter_values) * len(word)
    if len(word) == n:
        letter_values += 50
    return letter_values