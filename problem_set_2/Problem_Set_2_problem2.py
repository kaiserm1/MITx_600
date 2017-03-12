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
    counter = 0
    while True:
        unpaid_balance = balance
        for i in range(12):
            new_balance = unpaid_balance - lowest_payment_per_month
            unpaid_balance = new_balance + new_balance * monthly_interest_rate
        if unpaid_balance < 0:
            break
        lowest_payment_per_month += 10
    return lowest_payment_per_month
       
print("Lowest Payment:", lowest_payment(balance, annualInterestRate))