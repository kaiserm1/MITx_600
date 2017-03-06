# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:32:59 2017

@author: maka_
"""
s = "azcbobobegghakl"
counter = 0

for letter in s:
    if letter in "aeiou":
        counter += 1
        
print(counter)