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
    
    
    monthly_interest_rate = annualInterestRate / 12
    lowest_payment_per_month = 10
    
    def calculate_lowest_payment_rec(lowest_payment_per_month)
        if balance <= 0:
            return lowest_payment_per_month
        else:
            for i in range(12):
                new_balance = balance - lowest_payment_per_month
                balance = new_balance + new_balance * monthly_interest_rate
                lowest_payment_per_month += 10
                lowest_payment(balance, annualInterestRate)
    
   
print("Lowest Payment:", lowest_payment(balance, annualInterestRate))