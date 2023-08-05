# 
# a9task2.py - Assignment 9, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Backtesting your own Trading Strategy
# 
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch data
def fetch_data(file_name):
    """
    Reads data from the given CSV file. Parses the 'Date' column as DateTime 
    and sets it as the index of the DataFrame. Only uses the 'Adj Close' column.
    
    Arguments:
   - file_name (str): The path to the CSV file
   
   Returns:
   - pandas.DataFrame: DataFrame containing the 'Adj Close' column
   """
    data = pd.read_csv(file_name, parse_dates=['Date'], index_col='Date')
    # Use 'Adj Close' for calculations
    return data['Adj Close']

def trade_strategy(data, cash, trading_fee_fixed=None, trading_fee_pct=None):
    """
    Sell 1% of position when stock goes up, buy 1% when stock goes down.
    Apply trading fees/commissions if specified.

    Arguments:
    - data: DataFrame with historical price data
    - cash: Initial cash amount
    - trading_fee_fixed: Fixed trading fee per trade (default: None)
    - trading_fee_pct: Percentage trading fee per trade (default: None)
    """
    # Initialize shares with no holdings
    shares = pd.DataFrame(index=data.index, columns=data.columns)
    shares.iloc[0] = ((cash / 2) / len(data.columns)) / data.iloc[0]

    cash_account = pd.Series(0, index=data.index)
    cash_account[0] = cash - (shares.iloc[0] * data.iloc[0]).sum()

    # Iterate over each day
    for i in range(1, len(shares.index)):
        # Compute portfolio value
        portfolio_value = shares.loc[shares.index[i-1]] * data.loc[data.index[i]]

        # Adjust holdings based on stock performance
        shares.loc[shares.index[i]] = shares.loc[shares.index[i-1]]
        increase = data.loc[data.index[i]] > data.loc[data.index[i-1]]
        decrease = data.loc[data.index[i]] < data.loc[data.index[i-1]]
        
        #renew cash_account
        cash_account[i] = cash_account[i-1]

        # Sell 1% if stock goes up
        for column in shares.columns[increase]:
            sell_shares = shares.loc[shares.index[i-1], column] * 0.01
            shares.loc[shares.index[i], column] -= sell_shares
            cash_account[i] += sell_shares * data.loc[data.index[i], column]

        # Buy 1% if stock goes down
        for column in shares.columns[decrease]:
            if cash_account[i] > 0:
                buy_cash = cash_account[i] * 0.01
                buy_shares = buy_cash / data.loc[data.index[i], column]
                shares.loc[shares.index[i], column] += buy_shares
                cash_account[i] -= buy_cash

        # Apply trading fees
        if trading_fee_fixed is not None:
            trading_fees = len(data.columns) * trading_fee_fixed
        elif trading_fee_pct is not None:
            trading_fees = np.abs(shares.loc[shares.index[i-1]] - shares.loc[shares.index[i]]).sum() * trading_fee_pct
        else:
            trading_fees = 0
        # Update cash account after trading fees
        cash_account[i] -= trading_fees

    # Compute portfolio in terms of cash
    portfolio = shares * data
    portfolio['Cash'] = cash_account
    portfolio['Portfolio_Value'] = portfolio.sum(axis=1)

    return portfolio

def calculate_abnormal_return(portfolio, benchmark):
    """
    Calculate the abnormal return at each time point.
    
    Arguments:
    portfolio (pd.DataFrame): The portfolio value at each time point.
    benchmark (pd.DataFrame): The benchmark value at each time point.
    
    Returns:
    pd.Series: The abnormal returns at each time point.
    """
    # Calculate returns
    portfolio_returns = portfolio['Portfolio_Value'].pct_change()
    benchmark_returns = benchmark.pct_change()

    # Calculate the abnormal returns
    abnormal_returns = portfolio_returns - benchmark_returns

    return abnormal_returns

def draw_graphs(df):
    """
    Plots the portfolio value and a benchmark index (like SPY) over time in a dual-axis chart.

    Arguments:
    - df (pandas.DataFrame): DataFrame containing portfolio value and benchmark index
    """
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Portfolio Value', color=color)
    ax1.plot(df.index, df['Portfolio_Value'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('SPY', color=color)
    ax2.plot(df.index, df['SPY'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Portfolio Value and SPY Over Time')
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Abnormal_Return'])
    plt.xlabel('Date')
    plt.ylabel('Abnormal Return')
    plt.title('Abnormal Return Over Time')
    plt.show()

def compute_statistics(df):
    """
    Computes various statistics like mean return, standard deviation of return, and cumulative abnormal return.

    Arguments:
    - df (pandas.DataFrame): DataFrame containing 'Portfolio_Value' and 'SPY' columns

    Returns:
    - pandas.DataFrame: DataFrame containing the computed statistics for the portfolio and the benchmark (SPY)
    """
    
    # calculate rate of return
    df['Portfolio_Return'] = df['Portfolio_Value'].pct_change()
    df['SPY_Return'] = df['SPY'].pct_change()

    # calculate mean return and standard deviation
    mean_return_portfolio = df['Portfolio_Return'].mean()
    std_return_portfolio = df['Portfolio_Return'].std()

    mean_return_spy = df['SPY_Return'].mean()
    std_return_spy = df['SPY_Return'].std()

    # calculate cumulative abnormal returns
    df['Cumulative_Abnormal_Return'] = (1 + df['Abnormal_Return']).cumprod() - 1
    cumulative_abnormal_return = df['Cumulative_Abnormal_Return'].iloc[-1]

    # create results dataframe
    results_df = pd.DataFrame({
        'Mean_Return': [mean_return_portfolio, mean_return_spy],
        'Std_Return': [std_return_portfolio, std_return_spy],
        'Cumulative_Abnormal_Return': [cumulative_abnormal_return, None]
    }, index=['Portfolio', 'SPY'])

    return results_df

# Main function
def main():
    # Read data from CSV files
    aapl = fetch_data("/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/AAPL.csv")
    bac = fetch_data("/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/BAC.csv")
    goog = fetch_data("/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/GOOG.csv")
    spy = fetch_data("/Users/apple/Downloads/科科/MF602---Python-Refresher/assignment_3/SPY.csv")

    # Combine into single DataFrame
    data = pd.concat([aapl, bac, goog, spy], axis=1)
    data.columns = ["AAPL", "BAC", "GOOG", "SPY"]

    # Initial cash amount
    cash = 200000  # Adjust to your initial investment amount

    # Choose SPY as the benchmark
    benchmark = data['SPY']
    
    # Apply trading strategy without trading fees
    portfolio_no_fees = trade_strategy(data, cash)
    print("Portfolio without trading fees:")
    print(portfolio_no_fees)

    # Calculate abnormal return at each time point
    portfolio_no_fees['Abnormal_Return'] = calculate_abnormal_return(portfolio_no_fees, benchmark)
    
    print(portfolio_no_fees)

    draw_graphs(portfolio_no_fees)
    
    results_portfolio_no_fees = compute_statistics(portfolio_no_fees)
    print(results_portfolio_no_fees)

    # Apply trading strategy with fixed trading fee
    fixed_fee = 10
    portfolio_fixed_fee = trade_strategy(data, cash, trading_fee_fixed=fixed_fee)
    print(f"Portfolio with fixed trading fee of ${fixed_fee} per trade:")
    print(portfolio_fixed_fee)
    
    # Calculate abnormal return at each time point
    portfolio_fixed_fee['Abnormal_Return'] = calculate_abnormal_return(portfolio_fixed_fee, benchmark)
    
    print(portfolio_fixed_fee)

    draw_graphs(portfolio_fixed_fee)
    
    results_portfolio_fixed_fee = compute_statistics(portfolio_fixed_fee)
    print(results_portfolio_fixed_fee)

    # Apply trading strategy with percentage trading fee
    pct_fee = 0.0025
    portfolio_pct_fee = trade_strategy(data, cash, trading_fee_pct=pct_fee)
    print(f"Portfolio with {pct_fee*100}% trading fee per trade:")
    print(portfolio_pct_fee)
    
    # Calculate abnormal return at each time point
    portfolio_pct_fee['Abnormal_Return'] = calculate_abnormal_return(portfolio_pct_fee, benchmark)
    
    print(portfolio_pct_fee)

    draw_graphs(portfolio_pct_fee)
    
    results_portfolio_pct_fee = compute_statistics(portfolio_pct_fee)
    print(results_portfolio_pct_fee)

if __name__ == "__main__":
    main()
