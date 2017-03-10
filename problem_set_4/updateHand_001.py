# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:08:47 2017

@author: maka_
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    for letter in word:
        hand[letter] = hand.get(letter, 0) - 1
    return hand


