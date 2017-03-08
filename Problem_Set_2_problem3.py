# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:21:19 2017

@author: maka_
"""

def lowest_payment(balance, annualInterestRate):
    """
    Input: balance as float - the outstanding balance on the credit card
           annualInterestRate as float - annual interest rate as a decimal
    
    Calculate lowest payment per month with an accuracy of 0.01 using
    bisection search.
    """
    
    def new_guess(lower_boundary, upper_boundary):
        guess = (lower_boundary + upper_boundray) / 2
        return guess
    
    monthly_interest_rate = annualInterestRate / 12.0
    lower_boundary = balance / 12.0
    upper_boundary = (balance * (1 + monthly_interest_rate)**12) / 12.0
    epsilon = 0.01
    
    if abs(balance - (guess * 12)) <= epsilon:
        return guess
    else:
        if abs(balance - (guess * 12)) > epsilon:
            
        
    
   
print("Lowest Payment:", lowest_payment(balance, annualInterestRate))