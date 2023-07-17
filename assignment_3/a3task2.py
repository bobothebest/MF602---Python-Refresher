# 
# a3task2.py - Assignment 3, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#
from a3task1 import *


def calc_returns(prices):
    """ This function will process a list of stock prices and calculate the 
        periodic returns. The function should assume that the oldest price is 
        in prices[0] and latest price in prices[-1]. The function should use a 
        loop and accumulator pattern to accumulate a list of returns for 
        periods 1 to n – there is no return for period 0.
        input prices: a list of stock prices
    """
    n = len(prices)
    r = []
    for i in range(n-1):
        r.append(prices[i+1]/prices[i] - 1)
    return r

# function calc_returns(prices)
def process_stock_prices_csv(filename):
    """ This function will process a list of stock prices and calculate the 
        periodic returns. The function should assume that the oldest price is 
        in prices[0] and latest price in prices[-1]. The function should use a 
        loop and accumulator pattern to accumulate a list of returns for 
        periods 1 to n – there is no return for period 0.
        input prices: a list of stock prices
    """
    prices = []
    
    with open(filename) as file:
        # Discard the first line (header)
        header = file.readline()

        # Process the rest of the file
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespaces
            values = line.split(",")  # Split the line into values
            adj_close = float(values[-2])  # Get the "Adj Close" value and convert it to float
            prices.append(adj_close)  # Append the price to the list

    return prices

# function stock_report(filenames)
def stock_report(filenames):
    """ This program will process the list of filenames, each of which is 
        a .CSV file containing stock price data in the Yahoo Finance format 
        (for the same time periods), as well as the the stock market index (^SPC). 
        The finished version of the function must return a string containing 
        the entire report, i.e., several outputs, neatly formatted, etc.
        input filename: a list of file's paths
    """
    n = len(filenames)
    result = f"Calculated returns for {n} stocks.\n\n"
    
    result += "Descriptive statistics for daily stock returns:\n"
    result += "Symbol:     "
    
    l = []
    stock_returns = []
    m = []
    stds = []
    Symbol = []
    for filename in filenames:
        pos1 = filename.find('/',20)
        symbol = filename[pos1+1:-4]
        Symbol.append(symbol)
        result += f"{symbol:>10}"
        
        ll = process_stock_prices_csv(filename)
        l.append(ll)
        
        stock_return = calc_returns(ll)
        stock_returns.append(stock_return)
        
        mm = mean(stock_return)
        m.append(mm)
        
        std = stdev(stock_return)
        stds.append(std)
        
    y = stock_returns[-1]
    Covar = []
    Correl = []
    R_SQ = []
    Beta = []
    Alpha = []
    for i in range(4):
        cov = covariance(stock_returns[i],y)
        Covar.append(cov)
        
        corr = correlation(stock_returns[i],y)
        Correl.append(corr)
        
        r = rsq(stock_returns[i],y)
        R_SQ.append(r)
        
        re = simple_regression(stock_returns[i],y)
        b = re[1]
        Beta.append(b)
        a = re[0]
        Alpha.append(a)
        
    result += "\nMean:       "
    for mm in m:
        result += f"{mm:>10.5f}"

    result += "\nStDev:      "
    for std in stds:
        result += f"{std:>10.5f}"

    result += "\nCovar:      "
    for cov in Covar:
        result += f"{cov:>10.5f}"

    result += "\nCorrel:     "
    for corr in Correl:
        result += f"{corr:>10.5f}"

    result += "\nR-SQ:       "
    for r in R_SQ:
        result += f"{r:>10.5f}"

    result += "\nBeta:       "
    for b in Beta:
        result += f"{b:>10.5f}"

    result += "\nAlpha:      "
    for a in Alpha:
        result += f"{a:>10.5f}"
    return result

if __name__ == '__main__':
    # sample test call for function calc_returns(prices)
    prices = [100,110,105,112,115]
    print("calc_returns([100,110,105,112,115]) returned\n", calc_returns(prices))

    # sample test call for function process_stock_prices_csv(filename)
    filename = '/Users/apple/Downloads/AAPL.csv'
    prices = process_stock_prices_csv(filename)
    print("process_stock_prices_csv(filename) returned\n", process_stock_prices_csv(filename))

    # sample test call for function stock_report(filenames)
    filenames = ['/Users/apple/Downloads/AAPL.csv', '/Users/apple/Downloads/GOOG.csv', '/Users/apple/Downloads/BAC.csv', '/Users/apple/Downloads/SPY.csv']
    result = stock_report(filenames)
    print("stock_report(filenames) returned\n", stock_report(filenames))














