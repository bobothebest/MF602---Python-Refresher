# 
# a9task1.py - Assignment 9, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Bollinger Bands and Backtesting a Trading Strategy
# 
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# function create_bollinger_bands(df, window=21, no_of_std=1, column_name='')
def create_bollinger_bands(df, window=21, no_of_std=1, column_name=''):
    """
    Create Bollinger Bands for the given DataFrame.

    :param df: pandas.DataFrame, DataFrame containing one or more columns of numerical data observations.
    :param window: int, number of days to use in creating the rolling mean and standard deviation (default is 21).
    :param no_of_std: int, number of standard deviations to use in calculating the Bollinger bands (default is 1).
    :param column_name: str, name of the column to use from the DataFrame df. If not provided, use the first column of from the DataFrame (default is '').

    :return: pandas.DataFrame, DataFrame with the same index as the parameter df, containing the columns: ['Observations', 'RollingMean', 'LowerBound', 'UpperBound']
    """
    # if column_name is not provided, use the first column
    if not column_name:
        column_name = df.columns[0]

    # Calculate rolling mean and standard deviation
    rolling_mean = df[column_name].rolling(window).mean()
    rolling_std = df[column_name].rolling(window).std()

    # Calculate upper Bollinger Band and lower Bollinger Band
    upper_band = rolling_mean + no_of_std * rolling_std
    lower_band = rolling_mean - no_of_std * rolling_std

    # Create a new DataFrame to hold the Bollinger Bands data
    bollinger_bands = pd.DataFrame(index=df.index)
    bollinger_bands['Observation'] = df[column_name]
    bollinger_bands['RollingMean'] = rolling_mean
    bollinger_bands['UpperBound'] = upper_band
    bollinger_bands['LowerBound'] = lower_band

    return bollinger_bands

#function create_long_short_position(df)
def create_long_short_position(df):
    """
    Create long and short positions based on Bollinger Bands and keep the position until it crosses the other band.

    :param df: pandas.DataFrame object with the columns: ['Observation', 'RollingMean', 'LowerBound', 'UpperBound'].
    
    :return: pandas.DataFrame object with the same index as the parameter df, containing a column: ['Position'] where +1 indicates a long position and -1 indicates a short position.
    """
    # Initialize an empty DataFrame with the same index as df
    position = pd.DataFrame(index=df.index)
    
    # Create a column 'Position' initialized with 0 (no position)
    position['Position'] = 0
    
    # Create a long position (+1) when 'Observation' crosses above 'UpperBound'
    position.loc[df['Observation'] > df['UpperBound'], 'Position'] = 1
    
    # Create a short position (-1) when 'Observation' crosses below 'LowerBound'
    position.loc[df['Observation'] < df['LowerBound'], 'Position'] = -1
    
    # Forward fill Position column, such that a position is maintained until it crosses the other band
    position['Position'] = position['Position'].replace(0, np.nan).ffill().fillna(0)
    
    return position

#function calculate_long_short_returns(df, position, column_name='')
def calculate_long_short_returns(df, position, column_name=''):
    """
    Calculate market return, strategy return, and abnormal return based on the positions.

    :param df: pandas.DataFrame, DataFrame containing asset price data series.
    :param position: pandas.DataFrame, DataFrame with the same index as the parameter df, containing a column 'Position'
    :param column_name: str, name of the column to use from the DataFrame df, containing the asset prices. If not provided, use the first column of from the DataFrame (default is '').

    :return: pandas.DataFrame, DataFrame with the same index as the parameter df, containing the columns: ['Market Return', 'Strategy Return', 'Abnormal Return']
    """
    # if column_name is not provided, use the first column
    if not column_name:
        column_name = df.columns[0]

    # Calculate the daily returns for the market
    df['Market Return'] = df[column_name].pct_change()

    # Calculate the daily returns for the strategy
    df['Strategy Return'] = df['Market Return'] * position['Position'].shift()

    # Calculate the abnormal return
    df['Abnormal Return'] = df['Strategy Return'] - df['Market Return']

    # Create a new DataFrame to hold the results
    returns = df[['Market Return', 'Strategy Return', 'Abnormal Return']].copy()

    return returns

#function plot_cumulative_returns(df)
def plot_cumulative_returns(df):
    """
    Create a plot of the cumulative return for each column in df.

    :param df: pandas.DataFrame, DataFrame with one or more series of returns.
    """
    # Calculate cumulative returns
    cumulative_returns = (1 + df).cumprod() - 1

    # Plot the cumulative returns
    cumulative_returns.plot()
    plt.title('Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    
    # sample test call for create_bollinger_bands(df, window=21, no_of_std=1, column_name='')
    df = pd.read_csv('/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/AAPL.csv')
    df.index = df['Date']
    # obtain only a one-year slice:
    df = df.loc['2017-01-01':'2017-12-31']
    df.tail()
    
    bb = create_bollinger_bands(df, window = 10, no_of_std = 2, column_name = 'Adj Close')
    bb.tail()
    
    bb.plot() # creates the plot
    
    bb = create_bollinger_bands(df, window = 10, no_of_std = 2, column_name = 'High')
    bb.tail()
    
    # create a 1-column DataFrame
    df = pd.DataFrame(index=df.index, data = df['Close'])
    df.tail()
    bb = create_bollinger_bands(df) # using default parameters
    bb.tail()
    
    df = pd.read_csv('/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/SPY.csv')
    df.index = df['Date']
    df = df.loc['2017-09-01':'2017-12-31']
    bb = create_bollinger_bands(df, window = 30, no_of_std = 1, column_name = 'Volume')
    bb.plot()
    
    # sample test call for create_long_short_position(df)
    # read a csv file
    df = pd.read_csv('/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/SPY.csv')
    df.index = df['Date']
    # obtain only a one-year slice:
    df = df.loc['2017-01-01':'2017-12-31']
    bb = create_bollinger_bands(df, window = 10, no_of_std = 2, column_name = 'Adj Close')
    position = create_long_short_position(bb)
    position.plot()
    
    # sample test call for calculate_long_short_returns(df, position, column_name='')
    bb = create_bollinger_bands(df, 10, 2, 'Adj Close')
    position = create_long_short_position(bb)
    returns = calculate_long_short_returns(df, position, 'Adj Close')
    returns.plot()
    
    # sample test call for plot_cumulative_returns(df)
    plot_cumulative_returns(returns)
    
    
    
    
    
    
    
    
    
    
    
    
    