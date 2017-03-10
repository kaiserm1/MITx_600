# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:20:46 2017

@author: maka_
"""


def remaining_balance(balance, annualInterestRate, monthlyPaymentRate):
    """
    Input: balance as float - outstanding balance on credit card
       annualInterestRate as float - annual interest rate as a decimal
       monthlyPaymentRate as floast - minimum monthly payment rate as a decimal
    
    Calculate statements on the monthly payment and remaining balance.
    At the end of 12 months, print out the remaining balance with 2 decimal 
    digits accuracy.
    """
    
    monthly_interest_rate = annualInterestRate / 12.0
    #minimum_monthly_payment = monthlyPaymentRate * previous_balance
    #monthly_unpaid_balance = previous_balance - monthlyPaymentRate
    #updated_balance_each_month = monthly_unpaid_balance + \
    #                             monthly_interest_rate * monthly_unpaid_balance
    
    
    for i in range(12):
        monthly_payment = monthlyPaymentRate * balance
        monthly_unpaid_balance = balance - monthly_payment
        balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    
    return round(balance, 2)

print("Remaining balance:", remaining_balance(balance, annualInterestRate, monthlyPaymentRate))
    