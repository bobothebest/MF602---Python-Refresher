# 
# a6task1.py - Assignment 6, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

class Date:
    """Class to represent a date"""

    def __init__(self, new_month, new_day, new_year):
        """
        Constructor for Date objects
        defines the attributes that compose a Date object (month, day, and year)
        and accepts parameters to set an object’s attributes to some initial values.
        """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    def __repr__(self):
        """Returns a string representation of a Date object"""
        return f'{self.month:02d}/{self.day:02d}/{self.year:04d}'

    def copy(self):
        """Returns a newly-constructed object of type Date with the same month, day, and year"""
        return Date(self.month, self.day, self.year)
    
    def __eq__(self, other):
        """Compares two Date objects for equality"""
        if isinstance(other, Date):
            return self.day == other.day and self.month == other.month and self.year == other.year
        return False

    def is_leap_year(self):
        """Returns True if the Date is in a leap year, False otherwise"""
        if self.year % 4 != 0:
            return False
        elif self.year % 100 != 0:
            return True
        elif self.year % 400 != 0:
            return False
        else:
            return True
        
    def is_valid_date(self):
        """Returns True if the Date is valid, False otherwise"""
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1:
            return False
        if self.month in [4, 6, 9, 11] and self.day > 30:
            return False
        if self.month in [1, 3, 5, 7, 8, 10, 12] and self.day > 31:
            return False
        if self.month == 2:
            if self.is_leap_year() and self.day > 29:
                return False
            elif not self.is_leap_year() and self.day > 28:
                return False
        return True
    
    def add_one_day(self):
        """Advances the Date object by one day"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() and self.month == 2:
            days_in_month[2] = 29

        self.day += 1
        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
                
    def rem_one_day(self):
        """Regresses the Date object by one day"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() and self.month == 3:
            days_in_month[2] = 29
    
        self.day -= 1
        if self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.month = 12
                self.year -= 1
                self.day = days_in_month[self.month]
            else:
                self.day = days_in_month[self.month]
                
    def add_n_days(self, n):
        """Advances the Date object by n days"""
        for _ in range(n):
            self.add_one_day()
            #print(self)

    def rem_n_days(self, n):
        """Regresses the Date object by n days"""
        for _ in range(n):
            self.rem_one_day()
            
    def is_before(self, other):
        """Checks if the Date object occurs before another Date object"""
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False   

    def is_after(self, other):
        """Checks if the Date object occurs after another Date object"""
        return not (self == other or self.is_before(other))
    
    def diff(self, other):
        """Returns the number of days between the Date object and another Date object"""
        self_copy = self.copy()
        other_copy = other.copy()
        days = 0
    
        if self_copy.is_after(other_copy):
            while self_copy != other_copy:
                other_copy.add_one_day()
                days += 1
            return days
        else:
            while self_copy != other_copy:
                self_copy.add_one_day()
                days -= 1
            return days    
        
    def day_of_week(self):
        """Returns the day of the week of the Date object"""
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                             'Friday', 'Saturday', 'Sunday']
        known_monday = Date(4, 18, 2016)
        days_difference = self.diff(known_monday)
        return day_of_week_names[days_difference % 7]
    
    def __str__(self):
        """Returns a string representation of the date in the format MM/DD/YYYY."""
        return f"{self.month:02d}/{self.day:02d}/{self.year}"
        
    def string_to_date(date_string):
        """Converts a date string in the format MM/DD/YYYY to a Date object."""
        month, day, year = map(int, date_string.split('/'))
        return Date(month, day, year)

if __name__ == '__main__':
    ##test for __repr__ method
    # Create a Date object named d1 using the constructor.
    d1 = Date(7, 25, 2022)
    # An example of using the __repr__ method. Note that no quotes
    # are displayed, even though the function returns a string.
    d1
    
    d1 = Date(1, 1, 2022)
    d2 = d1
    d3 = d1.copy()

    ##test for __eq__ method
    # Determine the memory addresses to which the variables refer.
    id(d1)# Your memory address may differ.        
    id(d2)# d2 is a reference to the same Date that d1 references.
    id(d3)# d3 is a reference to a different Date in memory.            
    # The == operator tests whether memory addresses are equal.
    d1 == d2# Shallow copy -- d1 and d2 have the same memory address.             
    d1 == d3# Deep copy -- d1 and d3 have different memory addresses.
        
    ##test for is_leap_year(self) method
    # Create a Date object named d1 using the constructor.
    d1 = Date(1, 1, 2020)
    # Check if d1 is in a leap year -- it is!
    d1.is_leap_year()
    # Create another object named d2
    d2 = Date(1, 1, 2021)
    # Check if d2 is in a leap year.
    d2.is_leap_year()
    
    d3 = Date(1, 1, 2000)
    # Check if d3 is in a leap year -- it is!
    d3.is_leap_year()
    # Create another object named d4
    d4 = Date(1, 1, 2100)
    # Check if d4 is in a leap year.
    d4.is_leap_year()
    
    ##test for is_valid_date(self) method
    d1 = Date(7,25,2022)
    d1.is_valid_date()

    d2 = Date(14,25,2022)
    d2.is_valid_date()

    d3 = Date(2,30,2020)
    d3.is_valid_date()

    d4 = Date(2,29,2020)
    d4.is_valid_date()

    d5 = Date(2,29,2022)
    d5.is_valid_date()

    d6 = Date(-4,-4, -5)
    d6.is_valid_date()

    d7 = Date(2,29,2100)
    d7.is_valid_date()
    
    ##test for is_valid_date(self) method
    d = Date(7, 25, 2022) # an easy case first!
    d
    d.add_one_day()
    d

    d = Date(7, 31, 2022) # a more difficult case
    d
    d.add_one_day()
    d

    d = Date(12, 31, 2022) # a hard case
    d
    d.add_one_day()
    d

    d = Date(2, 28, 2020) # a harder case
    d.add_one_day()
    d
    d.add_one_day()
    d
    
    ##test for rem_one_day(self) method
    d = Date(7, 25, 2022) # a straightforward case
    d
    d.rem_one_day()
    d

    d = Date(8, 1, 2022) # a case where the month changes
    d
    d.rem_one_day()
    d

    d = Date(1, 1, 2022) # a case where the year changes
    d
    d.rem_one_day()
    d

    d = Date(3, 1, 2020) # a leap year case
    d
    d.rem_one_day()
    d
    d.rem_one_day()
    d
    
    d = Date(3, 1, 2021) # a normal year case
    d
    d.rem_one_day()
    d
    d.rem_one_day()
    d
    
    ##test for add_n_days(self, n) method
    d = Date(7, 25, 2022)
    d.add_n_days(3)
    d
    
    d = Date(7, 25, 2022)
    d.add_n_days(0)
    d
    
    ##test for rem_n_days(self, n) method
    d = Date(7, 28, 2022)  # straightforward case
    d
    d.rem_n_days(3)
    d

    d = Date(8, 1, 2022)  # case where the month changes
    d
    d.rem_n_days(2)
    d

    d = Date(1, 1, 2022)  # case where the year changes
    d
    d.rem_n_days(1)
    d

    d = Date(3, 1, 2020)  # leap year case
    d
    d.rem_n_days(1)
    d
    d.rem_n_days(1)
    d
    
    ##test for __eq__(self, other) method
    d1 = Date(1, 1, 2022)
    d2 = d1
    d3 = d1.copy()

    # Determine the memory addresses to which the variables refer.
    id(d1)               
    id(d2)         # d2 is a reference to the same Date that d1 references.
    id(d3)         # d3 is a reference to a different Date in memory.

    # The new == operator tests whether the internal date is the same.
    d1 == d2       # Both refer to the same object, so their internal
                   # data is also the same.
    d1 == d3       # These variables refer to different objects, but
                   # their internal data is the same!
                   
    ##test for is_before(self, other) method
    ny = Date(1, 1, 2023)
    d = Date(7, 25, 2022)
    ny.is_before(d)
    d.is_before(ny)
    d.is_before(d)

    d3 = Date(12,31,2022)
    d3.is_before(ny)

    d4 = Date(12,31,2023)
    d4.is_before(ny)
    
    ##test for is_after(self, other) method
    ny = Date(1, 1, 2023)
    d = Date(7, 25, 2022)
    ny.is_after(d)

    d.is_after(ny)

    d.is_after(d)

    d3 = Date(12,31,2022)
    d3.is_after(ny)

    d4 = Date(12,31,2023)
    d4.is_after(ny)

    d5 = Date(1, 1, 2022)
    d5.is_after(d)     

    ##test for diff(self, other) method
    d1 = Date(7, 25, 2022)
    d2 = Date(8, 1, 2022)
    d2.diff(d1)
    d1.diff(d2)
    d1           # Make sure the original objects did not change.
    d2

    #another example:
    d3 = Date(7, 25, 2022)
    d4 = Date(4, 17, 2023)
    d4.diff(d3)
    d3.diff(d4)

    # Here is an example that pass over a leap day.
    d5 = Date(2, 15, 2020)
    d6 = Date(3, 15, 2020)
    d6.diff(d5)   

    ##test for day_of_week(self) method
    d = Date(4, 17, 2023)
    d.day_of_week()
    Date(1, 1, 2100).day_of_week()
    Date(7, 4, 1776).day_of_week()
      
                   
                   
                   
                   
                   
                   
                   
                   
    
