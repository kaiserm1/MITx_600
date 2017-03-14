# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 10:45:26 2017

@author: maka_
"""
import string
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
#        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
#    def get_valid_words(self):
#        '''
#        Used to safely access a copy of self.valid_words outside of the class
#        
#        Returns: a COPY of self.valid_words
#        '''
#        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        self.shift = shift
        alphabet_lowercase = string.ascii_lowercase
        alphabet_uppercase = string.ascii_uppercase
        shift_dict = {}
        for i in range(len(alphabet_lowercase)):
            if i + shift > 25:
                index = i + shift - 26
            else:
                index = i + shift
            shift_dict[alphabet_lowercase[i]] = alphabet_lowercase[index]
            shift_dict[alphabet_uppercase[i]] = alphabet_uppercase[index]
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.shift = shift
        shift_dict = self.build_shift_dict(shift)
        alphabet = string.ascii_letters
        shifted_message = ""
        for letter in self.message_text:
            if letter in alphabet:
                shifted_message += shift_dict[letter]
            else:
                shifted_message += letter
        self.message_text = shifted_message[:]
        return self.message_text

test = Message("Martin")