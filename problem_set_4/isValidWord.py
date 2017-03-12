# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:35:51 2017

@author: maka_
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    import copy
    hand_copy = copy.deepcopy(hand)
    if word in wordList:
        try:
            for letter in word:
                if hand_copy[letter] - 1 < 0:
                    return False
                else:
                    hand_copy[letter] -= 1
        except:
            return False
        else:
            return True

        return True
    else:
        return False