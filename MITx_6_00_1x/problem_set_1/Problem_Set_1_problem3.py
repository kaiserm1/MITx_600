# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:50:28 2017

@author: maka_

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
"""
s = 'zyxwvutsrqponmlkjihgfedcba'
longest_sub_string = ""
for i in range(len(s)):
    sub_string = s[i]
    for j in range(i, len(s) - 1):
        if s[j] <= s[j + 1]:
            sub_string += s[j + 1]
            if len(sub_string) > len(longest_sub_string):
                longest_sub_string = sub_string[:]
        else:
            sub_string = s[j + 1] 
if longest_sub_string == "":
    longest_sub_string = s[0]
print("Longest substring in alphabetical order is: " + str(longest_sub_string))    
    