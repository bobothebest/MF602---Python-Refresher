# 
# a8task2.py - Assignment 8, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Quantifying Investment Risk, Part 2: Drawdown
# 
#
import pandas as pd
import matplotlib.pyplot as plt
from a7task1 import MCStockSimulator
import numpy as np

# function compute_drawdown(prices)
def compute_drawdown(prices):
    '''
    The function returns a pandas.DataFrame object containing these columns:
    price, which is a copy of the data in the parameter prices
    prev_max, which contains the previous peak price before this price,
    dd_dollars, which is the drawdown since the previous maximum price, measured in dollars,
    dd_pct, which is the percentage decline since the previous maximum price

    '''
    # Calculate the running maximum
    prices['prev_max'] = prices['Adj Close'].cummax()
    
    # Calculate drawdown in dollars
    prices['dd_dollars'] = prices['prev_max'] - prices['Adj Close']
    
    # Calculate drawdown in percentage
    prices['dd_pct'] = prices['dd_dollars'] / prices['prev_max']
    
    return prices

# function plot_drawdown(df)
def plot_drawdown(df):
    '''
    the function will create and show two charts:
    1 - The historical price and previous maximum price.
    2 - The drawdown since previous maximum price as a percentage lost.
    '''
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plot historical price and previous maximum price in the first subplot
    ax1.plot(df.index, df['Adj Close'], label='Price')
    ax1.plot(df.index, df['prev_max'], label='Previous Maximum')
    ax1.set_xlabel('Date')  # Set x-axis label
    ax1.set_title('Price and Previous Maximum')  # Set subplot title
    ax1.legend()

    # Plot drawdown percentage in the second subplot
    ax2.plot(df.index, df['dd_pct'], label='dd_pct')
    ax2.set_xlabel('Date')  # Set x-axis label
    ax2.set_title('Drawdown Percentage')  # Set subplot title
    ax2.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()
    
# function run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials)
def run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials):
    '''
    This function will use the Monte Carlo stock simulation that you wrote in 
    Assignment 7 to simulate the price path evoluation of a stock. Specifically,
    you will create an instance of the MCStockSimulator class, and run 
    num_trials, and calculate the maximum drawdown from each trial.

    The parameters are: init_price: the initial stock price at time 0 of the simulation,
    years: the number of years the simulation should run
    r: the mean annual rate of return,
    sigma: the standard deviation of annual returns,
    trial_size: the number of discrete steps per year, i.e., number of trading days,
    num_trials: the number of trials to include in this simulation run.

    The function returns a pd.Series object of the trial results (maximum drawdown of each trial).
    '''
    # Create an array to hold the maximum drawdown results
    results = np.zeros(num_trials)
    
    # Create an instance of the MCStockSimulator class
    mc_simulator = MCStockSimulator(init_price, years, r, sigma, trial_size)
    
    # Loop for the number of trials
    for i in range(num_trials):
        # Generate simulated stock values
        values = mc_simulator.generate_simulated_stock_values()

        # Calculate the drawdowns
        max_values = np.maximum.accumulate(values)
        drawdowns = 1 - values / max_values
        
        # Record the maximum drawdown
        results[i] = drawdowns.max()
    
    # Return a pandas Series of the results
    return pd.Series(results)



if __name__ == '__main__':
    # sample test call for compute_drawdown(prices)
    # Load the data
    df = pd.read_csv('/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/AAPL.csv')
    
    # Set 'Date' column as index
    df.index = pd.to_datetime(df['Date'])
    
    # Select only the 'Adj Close' price for the year 2017
    prices = df.loc['2017-01-01':'2017-12-31', ['Adj Close']]
    
    # Compute drawdown
    dd = compute_drawdown(prices)
    
    print(dd.describe())
    print(dd.tail(10))
    
    plot_drawdown(dd)
    
    # sample test call for plot_drawdown(df)
    plot_drawdown(dd)
    
    # sample test call for run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials)
    # Using historical AAPL prices
    df = pd.read_csv('/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/AAPL.csv')
    df['ret'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))    
    trial_size = 252 # trading days/year
    init_price = float(df['Adj Close'].sample())
    r = df['ret'].mean() * trial_size
    sigma = df['ret'].std() * np.sqrt(trial_size)
    years = 10
    num_trials = 100
    max_dd = run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials)
    max_dd.describe()
    max_dd.hist()
