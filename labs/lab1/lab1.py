"""
Name: <Olivia Bianco>
<lab1>.py

Problem: <Code to compute the monthly interest charge on a credit card account.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

def monthly_charge():
    annual_interest = eval(input("What is the annual interest rate?"))
    annual_rate = annual_interest / 100
    num_days = eval(input("What is the number of days in the billing cycle?"))
    prev_bal = eval(input("What is the previous net balance?"))
    step_one = num_days * prev_bal
    pay_amount = eval(input("What was the payment amount?"))
    pay_date = eval(input("When was this payment made?"))
    new_pay_date = num_days - pay_date
    step_two = pay_amount * new_pay_date
    step_three = step_one - step_two
    avg_daily_bal = step_three / num_days
    monthly_rate = annual_rate / 12
    monthly_charge = avg_daily_bal * monthly_rate
    return monthly_charge


print("The monthly interest charge is:", monthly_charge)
