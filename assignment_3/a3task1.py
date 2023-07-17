# 
# a3task1.py - Assignment 3, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#
import random
# function mean(values)
def mean(values):
    """ takes as a parameter a list of numbers, and calculates and returns 
        the mean of those values.
        input values: a list of numbers
    """
    n = len(values)
    s = 0
    for num in values:
        s = s + num
    return s/n

# function variance(values)
def variance(values):
    """ takes as a parameter a list of numbers, and calculates and returns 
        the population variance of the values in that list
        input values: a list of numbers
    """
    n = len(values)
    s = 0
    for num in values:
        s = s + (num - mean(values))**2
    return s/n

# function stdev(values)
def stdev(values):
    """ takes as a parameter a list of numbers, and calculates and returns 
        the population standard deviation of the values in that list. 
        The population standard deviation is the square-root of the population variance.
        input values: a list of numbers
    """
    return variance(values)**(1/2)

# function covariance(x,y)
def covariance(x,y):
    """ takes as parameters two lists of values, and calculates and returns 
        the population covariance for those two lists.  The population standard 
        deviation is the square-root of the population variance.
        input x: a list of numbers
        input y: a list of numbers
        the length of x and y should be the same
    """
    assert len(x) == len(y), "the length of x and y should be the same "
    n = len(x)
    cov = 0
    mx  = mean(x)
    my  = mean(y)
    for i in range(n):
        cov = cov + (x[i] - mx)*(y[i] - my)
    return cov/n

# function correlation(x,y)
def correlation(x,y):
    """ takes as parameters two lists of values, and calculates and returns 
        the correlation coefficient between these data series. 
        input x: a list of numbers
        input y: a list of numbers
        the length of x and y should be the same
    """
    assert len(x) == len(y), "the length of x and y should be the same "
    return covariance(x,y)/(stdev(x)*stdev(y))

# function rsq(x,y) 
def rsq(x,y):
    """ takes as parameters two lists of values, and calculates and returns 
        the square of the correlation between those two data series, 
        which is a measure of the goodness of fit measure to explain variation 
        in y as a function of variation of x.
        input x: a list of numbers
        input y: a list of numbers
        the length of x and y should be the same
    """
    assert len(x) == len(y), "the length of x and y should be the same "
    return correlation(x,y)**2

# function simple_regression(x,y)
def simple_regression(x,y):
    """ takes as parameters two lists of values, and calculates and returns 
        the regression coefficients between these data series. The function 
        should return a list containing two values: the intercept and 
        regression coefficients, α and β.
        input x: a list of numbers
        input y: a list of numbers
        the length of x and y should be the same
    """
    assert len(x) == len(y), "the length of x and y should be the same "
    beta = covariance(x,y)/variance(x)
    alpha = mean(y) - beta*mean(x)
    return [alpha, beta]

if __name__ == '__main__':
    # sample test call for function mean(values)
    x = [4,4,3,6,7]
    print("mean([4,4,3,6,7]) returned", mean(x))
    
    # sample test call for function variance(values)
    print("variance([4,4,3,6,7]) returned", variance(x))
    
    # sample test call for function stdev(values)
    print("stdev([4,4,3,6,7]) returned", stdev(x))
    
    # sample test call for function covariance(x,y)
    x = [4,4,3,6,7]
    y = [6,7,5,10,12]
    print("covariance([4,4,3,6,7],[6,7,5,10,12]) returned", covariance(x,y))
    
    # sample test call for function correlation(x,y)
    print("correlation([4,4,3,6,7],[6,7,5,10,12]) returned", correlation(x,y))
    print("correlation(list(range(10)), list(range(10,0,-1))) returned", correlation(list(range(10)), list(range(10,0,-1))))
    
    # sample test call for function rsq(x,y) 
    print("rsq([4,4,3,6,7],[6,7,5,10,12]) returned", rsq(x,y))

    """ Additional Example: 
        we expect no correlation and very low r-square between randomly selected 
        data values. This test uses two lists of random numbers. Notice the very 
        low r-squared.
    """
    a = list(range(30))
    b = list(range(30))
    random.shuffle(a)
    random.shuffle(b)
    print(a)
    print(b)
    print("correlation(a,b) returned", correlation(a,b))
    print("rsq(a,b) returned", rsq(a,b))
    
    # sample test call for simple_regression(x,y)
    print("simple_regression([4,4,3,6,7],[6,7,5,10,12]) returned", simple_regression(x,y))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
