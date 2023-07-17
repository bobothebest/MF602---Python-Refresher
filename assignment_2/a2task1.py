# 
# a2task1.py - Assignment 2, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Decision Statements
# 
#
# function smaller(x, y)
def smaller(x, y):
    """ takes two numbers x and y and returns the smaller of the two numbers
        input x: any number(int or float)
        input y: any number(int or float)
    """
    if x < y:
        return x
    else:
        return y

# function smallest(x, y, z) 
def smallest(x, y, z):
    """ takes three parameters and returns the smallest of the three
        input x: any number(int or float)
        input y: any number(int or float)
        input z: any number(int or float)
    """
    if smaller(x, y) < smaller(y, z):
        return smaller(x, y)
    else:
        return smaller(y, z)

# function is_factor(n, x) 
def is_factor(n, x):
    """ takes a two integers n and x, and returns True if x is a factor of n 
        and False otherwise.
        input n: any number(int)
        input x: any number(int)
    """
    return (n/x % 1 == 0)

# function  has_vowel(s)
def  has_vowel(s):
    """ takes a string s and returns True if the string contains at least 
        one vowel (any letter in 'aeiou') and False otherwise.
        input s: a string
    """
    if 'a' in s:
        return True
    elif 'e' in s:
        return True
    elif 'i' in s:
        return True
    elif 'o' in s:
        return True
    elif 'u' in s:
        return True
    else:
        return False


# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':

    # sample test call for function smaller(x, y)
    print('smaller(20, 4) returns', smaller(20, 4))
    print('smaller(5, 8) returns', smaller(5, 8))
    
    # sample test call for function smallest(x, y, z) 
    print('smallest(20, 4, 17) returns', smallest(20, 4, 17))
    print('smallest(10, 8, 4) returns', smallest(10, 8, 4))
    print('smallest(10, 8, 10) returns', smallest(10, 8, 10))
    print('smallest(10, 18, 10) returns', smallest(10, 18, 10))
    
    # sample test call for function is_factor(n, x) 
    print('is_factor(20, 4) returns', is_factor(20, 4))
    print('is_factor(4321, 13) returns', is_factor(4321, 13))
    print('is_factor(5338, 17) returns', is_factor(5338, 17))
    
    # sample test call for function has_vowel(s)
    print("has_vowel('finance') returns", has_vowel('finance'))
    print("has_vowel('czyk') returns", has_vowel('czyk'))
    
    
    
    
    

    
