# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:19:57 2017

@author: maka_
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())