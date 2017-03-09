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
    
    monthly_interest_rate = annualInterestRate / 12.0
    lower_boundary = balance / 12.0
    upper_boundary = (balance * (1 + monthly_interest_rate)**12) / 12
    epsilon = 0.01  
    guess = (lower_boundary + upper_boundary) / 2      
    
    
    while True:
        rest_balance = balance
        
        for i in range(12):
            new_balance = rest_balance - guess
            rest_balance = new_balance + new_balance * monthly_interest_rate
            
        if abs(rest_balance) <= epsilon:
            return guess
        
        elif rest_balance > epsilon:
            lower_boundary = guess
            guess = (lower_boundary + upper_boundary) / 2
        
        else:
            upper_boundary = guess
            guess = (lower_boundary + upper_boundary) / 2
    

print("Lowest Payment:", round(lowest_payment(balance, annualInterestRate), 2))
