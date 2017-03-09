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
            
    
    while abs(balance) > epsilon:
        for i in range(12):
            new_balance = balance - guess
            balance = new_balance + new_balance * monthly_interest_rate
        print(balance)
        if balance < -epsilon:
            upper_boundary = guess
            guess = (lower_boundary + upper_boundary) / 2
        else:
            lower_boundary = guess
            guess = (lower_boundary + upper_boundary) / 2
        
        
    return guess
    

    
        
b1 = 320000
a1 = 0.2

b2 = 999999
a2 = 0.18

print("Lowest Payment:", round(lowest_payment(b1, a1), 2))
print("Lowest Payment:", round(lowest_payment(b2, a2), 2))
#Lowest Payment: 29157.09
#Lowest Payment: 90325.03