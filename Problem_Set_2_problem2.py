# -*- coding: utf-8 -*-

"""
Created on Tue Mar  7 19:29:44 2017
@author: maka_

Problem 2 - Paying Debt Off in a Year
"""

def lowest_payment(balance, annualInterestRate):
    """
    Input: balance as float - the outstanding balance on the credit card
           annualInterestRate as float - annual interest rate as a decimal
    
    Calculate lowest payment per month as a multiple of $10 to pay of balance
    within a year.
    """
    
    
    monthly_interest_rate = annualInterestRate / 12.0
    lowest_payment_per_month = 10
    
    while balance >= 0:
        for i in range(12):
            new_balance = balance - lowest_payment_per_month
            balance = new_balance + new_balance * monthly_interest_rate
        lowest_payment_per_month += 10
        print(lowest_payment_per_month)
    return lowest_payment_per_month
    
   
print("Lowest Payment:", lowest_payment(balance, annualInterestRate))