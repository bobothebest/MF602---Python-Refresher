# 
# a1task4.py - Assignment 1, Task 4
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: The Life-Cycle Model of Saving and Consumption
# 
#

from a1task3 import *

def life_cycle_model():
    """
    Interacts with the user to collect inputs and display outputs related to the Life-Cycle Model of Saving and Consumption.
    Assumes working in real (inflation-adjusted dollars) and uses an inflation-adjusted risk-free interest rate.
    Simplification: Assumes no taxes.
    """
    # Collect user inputs
    r = float(input("Enter the current inflation-indexed risk-free rate of return: "))
    age_now = int(input("Enter your age now: "))
    retirement_age = int(input("Enter your expected retirement age: "))
    current_income = int(input("Enter your current annual income: "))

    # Calculate remaining working years and print results
    remaining_working_years = retirement_age - age_now
    print(f"\nYou have {remaining_working_years} remaining working years with an income of ${current_income} per year.")

    # Calculate human capital using pv_annuity function
    human_capital = pv_annuity(r, remaining_working_years, current_income)
    print(f"The present value of your human capital is about ${human_capital:.0f}")

    # Prompt the user for their current assets
    current_assets = int(input("Enter the value of your financial assets: "))
    economic_net_worth = human_capital + current_assets
    print(f"Your economic net worth is: ${economic_net_worth:.0f}")

    # Calculate sustainable standard of living
    consumption_years = 100 - age_now
    sustainable_annual_consumption = annuity_payment(r, consumption_years, economic_net_worth)
    print(f"\nYour sustainable standard of living is about ${sustainable_annual_consumption:.0f} per year.")

    # Calculate annual savings
    annual_savings = current_income - sustainable_annual_consumption
    print(f"To achieve this standard of living to age 100, you must save ${annual_savings:.0f} per year.")

if __name__ == '__main__':
    life_cycle_model()
