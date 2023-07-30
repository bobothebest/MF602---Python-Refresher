# 
# a7task1.py - Assignment 7, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#
import numpy as np
import matplotlib.pyplot as plt

class MCStockSimulator:
    """Class to do Monte Carlo Simulation """
    def __init__(self, s, t, r, sigma, nper_per_year):
        '''
        s (the current stock price in dollars),
        t (the option maturity time in years),
        r (the annualized rate of return on this stock),
        sigma (the annualized standard deviation of returns),
        nper_per_year (the number of discrete time periods per year)
    
        '''
        self.s = s
        self.t = t
        self.r = r
        self.sigma = sigma 
        self.nper_per_year = nper_per_year

    def __repr__(self):
        '''
        Returns a string representation of a MCStockSimulator object
        '''
        return f"StockSimulator (s=${self.s:.2f}, t={self.t:.2f} (years), r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year})"
    
    def generate_simulated_stock_returns(self):
        '''
        generate and return a np.array (numpy array) containing a sequence 
        of simulated stock returns over the time period t.
        '''
        dt = 1.0 / self.nper_per_year
        n = int(self.t * self.nper_per_year)
        returns = np.random.normal((self.r - 0.5 * self.sigma**2) * dt, self.sigma * np.sqrt(dt), n)
        return returns
    
    def generate_simulated_stock_values(self):
        '''
        generate and return a np.array (numpy array) containing a sequence 
        of stock values, corresponding to a random sequence of stock return.
        '''
        returns = self.generate_simulated_stock_returns()
        values = []
        values.append(self.s)
        for i in range(len(returns)):
            values.append(values[i] * np.exp(returns[i]))
        return values
    
    def plot_simulated_stock_values(self, num_trials=1):
        '''
        generate a plot of of num_trials series of simulated stock returns. 
        num_trials is an optional parameter; if it is not supplied, the default
        value of 1 will be used.
        '''
        plt.figure(figsize=(10,6))
        for _ in range(num_trials):
            values = self.generate_simulated_stock_values()
            plt.plot(values)
        plt.title(f'{num_trials} simulated trials')
        plt.xlabel('years')
        plt.ylabel('$ Value')
        plt.show()
    
if __name__ == '__main__':
    ##test for __repr__ method
    # initial stock price = $100; 1 year time frame
    # expected rate of return = 10%; standard deviation = 30%; 
    # 250 discrete time periods per year
    sim = MCStockSimulator(100, 1, 0.1, 0.3, 250)
    print(sim)
    
    ##test for generate_simulated_stock_returns(self) method
    sim = MCStockSimulator(100, 1, 0.10, 0.30, 2)
    sim.generate_simulated_stock_returns()

    sim = MCStockSimulator(100, 1, 0.10, 0.30, 4)
    sim.generate_simulated_stock_returns()
    
    sim = MCStockSimulator(100, 0.5, 0.10, 0.30, 2)
    sim.generate_simulated_stock_returns()
    
    sim = MCStockSimulator(100, 5, 0.10, 0.30, 250)
    returns = sim.generate_simulated_stock_returns()
    len(returns)
    
    ##test for generate_simulated_stock_values(self) method
    sim = MCStockSimulator(100, 1, 0.10, 0.30, 4)
    t1 = sim.generate_simulated_stock_values()
    
    sim = MCStockSimulator(100, 2, 0.10, 0.30, 24)
    sim.generate_simulated_stock_values()
    
    ##test for plot_simulated_stock_values(self, num_trials=1) method
    sim = MCStockSimulator(100, 2, 0.10, 0.30, 24)
    sim.plot_simulated_stock_values()
    
    sim = MCStockSimulator(100, 2, 0.10, 0.30, 250)
    sim.plot_simulated_stock_values(5)
    
    
    





