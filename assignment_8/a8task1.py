# 
# a8task1.py - Assignment 8, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Quantifying Investment Risk, Part 1: Value at Risk
# 
#

from scipy.stats import norm
import numpy as np
import pandas as pd


# function compute_model_var_pct(mu, sigma, x, n)
def compute_model_var_pct(mu, sigma, x, n):
    """ 
    this function compute the value at risk as a percentage of the asset/portfolio value.
    The function must return the value at risk as a floating point number.
    
    input mu: any number(int or float)
    input sigma: any number(int or float)
    input x: any number between 0 and 1(float)
    input n: any number(int)
    """
    # calculate Z-score from confidence level
    Z = norm.ppf(1 - x)

    # calculate VaR
    VaR = mu * n + Z * sigma * (n ** 0.5)

    # return VaR as a percentage
    return VaR

# function compute_historical_var_pct(returns, x, n)
def compute_historical_var_pct(returns, x, n):
    '''
    this function compute the VaR (as a percentage) using the historical simulation approach.
    The function must return the value at risk as a floating point number.
    
    input returns: The parameter returns is a Pandas Series containing 
                    historical daily stock returns, with a date index.
    input x: any number between 0 and 1(float)
    input n: any number(int)
    '''
    # Sort the returns in ascending order
    sorted_returns = returns.sort_values()

    # Calculate the index corresponding to the worst return
    index = int((1 - x) * len(sorted_returns))
    
    # Get the return at the calculated index
    var_1d = sorted_returns.iloc[index]

    # Scale the 1-day VaR to n-day VaR
    var_nd = var_1d * np.sqrt(n)

    # Return VaR as a percentage
    return var_nd

    
    
if __name__ == '__main__':

    # sample test call for compute_model_var_pct(mu, sigma, x, n)
    # estimate the 10-day VaR (98% confidence) 
    # using a mean daily return of 0.0008 and standard deviaton of 0.01
    print(compute_model_var_pct(0.0008, 0.01, 0.98, 10))  
    # estimate the 14-day VaR (97% confidence) 
    # using a mean daily return of 0.001 and standard deviaton of 0.015
    print(compute_model_var_pct(0.001, 0.015, 0.97, 14))
    
    
    # sample test call for compute_model_var_pct(mu, sigma, x, n)
    df = pd.read_csv('/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/AAPL.csv')
    # Calculate the daily returns
    df['Return'] = df['Adj Close'].pct_change()
    
    # Drop the missing values
    df = df.dropna()
    
    # Now, df['Return'] is a Pandas Series with daily returns
    returns = df['Return']
    
    print(compute_historical_var_pct(returns, 0.98, 7))  # -0.0769 (depends on your data)
    print(compute_historical_var_pct(returns, 0.99, 10))  # -0.1456 (depends on your data)


    
    
