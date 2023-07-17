# 
# a2task2.py - Assignment 2, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

# function mult(n, m)
def mult(n, m):
    """ takes two integers n and m as inputs and uses recursion to compute 
        and return the product of those integers.
        input n: any number(int)
        input m: any number(int)
    """
    if n == 0:
        return 0
    elif n < 0:
        return -mult(-n, m)
    else:
        return mult(n-1, m) + m

# function copy(s, n)
def copy(s, n):
    """ takes as inputs a string s and an integer n, and that uses recursion 
        to create and return a string in which n copies of s have been 
        concatenated together. If n is less than or equal to 0, the function 
        should return the empty string (i.e., the string ‘’, which does not 
        have any spaces between the quotes).
        input s: a string
        input n: any number(int)
    """
    if n <= 0:
        return ''
    else:
        return copy(s, n-1) + s

# function double(s)
def double(s):
    """ takes an arbitrary string s as input, and that uses recursion to 
        construct and return the string formed by doubling each character 
        in the string
        input s: a string
    """
    n = len(s)
    if n == 0:
        return ''
    else:
        t = s[n-1]
        s = s[:n-1]
        return double(s) + 2*t
    
# function dot(l1, l2)
def dot(l1, l2):
    """ takes as inputs two lists of numbers, l1 andl2, and uses recursion to 
        compute and return the dot product of those lists – i.e., the sum of 
        the products of the elements in the same positions in the two lists.
        For example, the dot product of [1, 2, 3] and [4, 5, 6] is 
        1*4 + 2*5 + 3*6 or 32.
        input l1: a lists of numbers
        input l2: a lists of numbers
    """
    #l1 = list(map(float, l1[:]))
    #l2 = list(map(float, l2[:]))
    n1 = len(l1)
    n2 = len(l2)
    if (n1 != n2) or (n1 == 0) or (n2 == 0):
        return 0.00
    else:
        t1 = l1[n1-1]
        l1 = l1[:n1-1]
        t2 = l2[n2-1]
        l2 = l2[:n2-1]
        return dot(l1, l2) + t1*t2

# function find_min(items)
def find_min(items):
    """ uses recursion to find the minimum from a list of items.
        For a list of numbers, the minimum will be the smallest number.
        For a list of strings, the minimum will be the string closest to the 
        start of the alphabet.
        input items: a lists of numbers or strings
    """
    n = len(items)
    if n == 1:
        return items[0]
    else:
        
        return min(items[0], find_min(items[1:]))

# function weave(s1, s2)
def weave(s1, s2):
    """ takes as inputs two strings s1 and s2 and uses recursion to construct 
        and return a new string that is formed by “weaving” together the 
        characters in the strings s1 and s2 to create a single string.

        In other words, the new string should alternate characters from the 
        two strings: the first character from s1, followed by the first character 
        from s2, followed by the second character from s1, followed by the 
        second character from s2, etc.

        If one of the strings is longer than the other, its “extra” characters 
        – the ones with no counterparts in the shorter string – should appear 
        immediately after the “woven” characters (if any) in the new string.
        
        input s1: a string
        input s2: a string
    """
    n1 = len(s1)
    n2 = len(s2)
    if n1 == n2 == 0:
        return ''
    elif n1 == 0:
        return s2
    elif n2 == 0:
        return s1
    elif n1 != n2:
        n = min(n1,n2)
        return weave(s1[:n], s2[:n]) + s1[n:] + s2[n:]
    else:
        return s1[0] + s2[0] + weave(s1[1:], s2[1:])

if __name__ == '__main__':
    """ test function for the functions above """
    # sample test call for function mult(x, y)
    test1_1 = mult(6, 7)
    print('the test1_1 returns', test1_1)
    test1_2 = mult(-3, 6)
    print('the test1_2 returns', test1_2)
    
    # sample test call for function copy(s, n)
    test2_1 = copy('da', 2)
    print('the test2_1 returns', "'%s'"%(test2_1))
    test2_2 = copy('Go BU!', 4)
    print('the test2_2 returns', "'%s'"%(test2_2))
    test2_3 = copy('hello', 1)
    print('the test2_3 returns', "'%s'"%(test2_3))
    test2_4 = copy('hello', 0)
    print('the test2_4 returns', "'%s'"%(test2_4))
    test2_5 = copy('hello', -7)
    print('the test2_5 returns', "'%s'"%(test2_5))
    
    # sample test call for function double(s)
    test3_1 = double('hello')
    print('the test3_1 returns', "'%s'"%(test3_1))
    test3_2 = double('python')
    print('the test3_2 returns', "'%s'"%(test3_2))
    test3_3 = double('')
    print('the test3_3 returns', "'%s'"%(test3_3))
    
    # sample test call for function dot(l1, l2)
    test4_1 = dot([5, 3], [6, 4])
    print('the test4_1 returns', test4_1)
    test4_2 = dot([1, 2, 3, 4], [10, 100, 1000, 10000])
    print('the test4_2 returns', test4_2)
    test4_3 = dot([5, 3], [6])
    print('the test4_3 returns', test4_3)
    
    # sample test call for function find_min(items)
    test5_1 = find_min([14,8,7,12])
    print('the test5_1 returns', test5_1)
    test5_2 = find_min(['z','h','e','l','m','c','s'])
    print('the test5_2 returns', "'%s'"%(test5_2))
    test5_3 = find_min([42])
    print('the test5_3 returns', test5_3)

    # sample test call for function weave(s1, s2)
    test6_1 = weave('aaaaaa', 'bbbbbb')
    print('the test6_1 returns', "'%s'"%(test6_1))
    test6_2 = weave('abcde', 'VWXYZ')
    print('the test6_2 returns', "'%s'"%(test6_2))
    test6_3 = weave('aaaaaa', 'bb')
    print('the test6_3 returns', "'%s'"%(test6_3))
    test6_4 = weave('aaaa', 'bbbbbb')
    print('the test6_4 returns', "'%s'"%(test6_4))
    test6_5 = weave('aaaa', '')
    print('the test6_5 returns', "'%s'"%(test6_5))
    test6_6 = weave('', 'bbbb')
    print('the test6_6 returns', "'%s'"%(test6_6))
    test6_7 = weave('', '')
    print('the test6_7 returns', "'%s'"%(test6_7))

