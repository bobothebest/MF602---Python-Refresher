# 
# a6task2.py - Assignment 6, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#
from a6task1 import Date

def options_expiration_days(year):
    """Returns a list of all of the Dates on which options expire during a calendar year."""
    options_expiration_dates = []
    for month in range(1, 13):  # For each month in the year
        date = Date(month, 15, year)
        while date.day_of_week() != 'Friday':  # Until we reach Friday
            date.add_one_day()
        options_expiration_dates.append(str(date))
    return options_expiration_dates

def market_holidays(year):
    """Returns a list of all of the Dates of US market holidays for a given year."""
    holidays = []

    # New Year’s Day
    new_years = Date(1, 1, year)
    if new_years.day_of_week() == 'Sunday':
        new_years.add_one_day()
    print(f"New Year's Day is observed on {new_years}")
    holidays.append(str(new_years))

    # Martin Luther King Day
    mlk_day = Date(1, 15, year)
    while mlk_day.day_of_week() != 'Monday':
        mlk_day.add_one_day()
    print(f"Martin Luther King Day is observed on {mlk_day}")
    holidays.append(str(mlk_day))

    # President’s Day
    presidents_day = Date(2, 15, year)
    while presidents_day.day_of_week() != 'Monday':
        presidents_day.add_one_day()
    print(f"President's Day is observed on {presidents_day}")
    holidays.append(str(presidents_day))

    # Memorial Day
    memorial_day = Date(5, 31, year)
    while memorial_day.day_of_week() != 'Monday':
        memorial_day = Date(memorial_day.month, memorial_day.day - 1, memorial_day.year)
    print(f"Memorial Day is observed on {memorial_day}")
    holidays.append(str(memorial_day))

    # Independence Day
    independence_day = Date(7, 4, year)
    if independence_day.day_of_week() == 'Sunday':
        independence_day.add_one_day()
    print(f"Independence Day is observed on {independence_day}")
    holidays.append(str(independence_day))

    # Labor Day
    labor_day = Date(9, 1, year)
    while labor_day.day_of_week() != 'Monday':
        labor_day.add_one_day()
    print(f"Labor Day is observed on {labor_day}")
    holidays.append(str(labor_day))

    # Thanksgiving Day
    thanksgiving_day = Date(11, 22, year)
    while thanksgiving_day.day_of_week() != 'Thursday':
        thanksgiving_day.add_one_day()
    print(f"Thanksgiving Day is observed on {thanksgiving_day}")
    holidays.append(str(thanksgiving_day))

    # Christmas Day
    christmas_day = Date(12, 25, year)
    if christmas_day.day_of_week() == 'Sunday':
        christmas_day.add_one_day()
    print(f"Christmas Day is observed on {christmas_day}")
    holidays.append(str(christmas_day))

    return holidays

if __name__ == '__main__':
    ##test for function options_expiration_days(year)
    options_expiration_days(2020)
    options_expiration_days(2021)   
    
    ##test for function market_holidays(year)
    holidays = market_holidays(2020)
    holidays
    holidays = market_holidays(2021)
    holidays
    
    
    
    
    
    
    