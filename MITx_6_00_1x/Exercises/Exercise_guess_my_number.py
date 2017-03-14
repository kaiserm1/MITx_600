# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:50:28 2017

@author: maka_
"""

print("Please think of a number between 0 and 100!")

low = 0
high = 100

ans = (low + high) // 2
    
while True:
    print("Is your secret number: " + str(ans) +"?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while answer not in ("hlc"):
        print("Sorry, I did not understand your input.")
        print("Is your secret number: " + str(ans) +"?")
        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if answer == "h":
        high = ans
        ans = (low + high) // 2
    elif answer == "l":
        low = ans
        ans = (low + high) // 2
    else:
        print("Game over. Your secret number was: " + str(ans))
        break
