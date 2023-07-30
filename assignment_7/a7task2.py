# 
# a7task2.py - Assignment 7, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

from a7task1 import MCStockSimulator
import numpy as np
import math

class MCStockOption(MCStockSimulator):
    """inherits from MCStockSimulator"""
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        '''
        s, which is the initial stock price
        x, which is the option’s exercise price
        t, which is the time to maturity (in years) for the option
        r, which is the (expected) mean annual rate of return on the underlying stock
        sigma, which is the annual standard deviation of returns on the underlying stock
        nper_per_year, which is the number of discrete time periods per year with which to evaluate the option, and
        num_trials, which is the number of trials to run when calculating the value of this option
    
        '''
        super().__init__(s, t, r, sigma, nper_per_year)
        self.x = x
        self.num_trials = num_trials

    def __repr__(self):
        '''
        Returns a string representation of a MCStockOption object
        '''
        return (f'MCStockOption, s={self.s:.2f}, x={self.x:.2f}, t={self.t:.2f}, '
                f'r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, '
                f'num_trials={self.num_trials}')
    
    def value(self):
        '''
        return the value of the option. 
        '''
        print("Base class MCStockOption has no concrete implementation of .value().")
        return 0

    def stderr(self):
        '''
        return the standard error of this option’s value. The standard error is
        calculated as stdev / sqrt(num_trials), where stdev is the standard 
        deviation of the values obtained from many trials.
        '''
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0
    
    
class MCEuroCallOption(MCStockOption):
    """ inherits from the base class MCStockOption"""
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def __repr__(self):
        return (f'MCEuroCallOption, s={self.s:.2f}, x={self.x:.2f}, t={self.t:.2f}, '
                f'r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, '
                f'num_trials={self.num_trials}')

    def value(self):
        self.values = []
        for _ in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            payoff = max(stock_values[-1] - self.x, 0)
            self.values.append(payoff)
        value = np.exp(-self.r * self.t) * np.mean(self.values)
        return value
    
    def stderr(self):
        sample_std = np.std(self.values)
        return sample_std / np.sqrt(self.num_trials)
        
    
class MCEuroPutOption(MCStockOption):
    """inherits from the base class MCStockOption"""
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def __repr__(self):
        return (f'MCEuroPutOption, s={self.s:.2f}, x={self.x:.2f}, t={self.t:.2f}, '
                f'r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, '
                f'num_trials={self.num_trials}')

    def value(self):
        self.values = []
        for _ in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            payoff = max(self.x - stock_values[-1], 0)
            self.values.append(payoff)
        value = np.exp(-self.r * self.t) * np.mean(self.values)
        return value
    
    def stderr(self):
        sample_std = np.std(self.values)
        return sample_std / np.sqrt(self.num_trials)
    
    
class MCAsianCallOption(MCStockOption):
    """Inherits from the base class MCStockOption."""
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def __repr__(self):
        return (f'MCAsianCallOption, s={self.s:.2f}, x={self.x:.2f}, t={self.t:.2f}, '
                f'r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, '
                f'num_trials={self.num_trials}')

    def value(self):
        self.values = []
        for _ in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            average_stock_price = np.mean(stock_values)
            payoff = max(average_stock_price - self.x, 0)
            self.values.append(payoff)
        value = np.exp(-self.r * self.t) * np.mean(self.values)
        return value

    def stderr(self):
        sample_std = np.std(self.values)
        return sample_std / np.sqrt(self.num_trials)
    
class MCAsianPutOption(MCStockOption):
    """Inherits from the base class MCStockOption."""
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def __repr__(self):
        return (f'MCAsianPutOption, s={self.s:.2f}, x={self.x:.2f}, t={self.t:.2f}, '
                f'r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, '
                f'num_trials={self.num_trials}')

    def value(self):
        self.values = []
        for _ in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            average_stock_price = np.mean(stock_values)
            payoff = max(self.x - average_stock_price, 0)
            self.values.append(payoff)
        value = np.exp(-self.r * self.t) * np.mean(self.values)
        return value

    def stderr(self):
        sample_std = np.std(self.values)
        return sample_std / np.sqrt(self.num_trials)
    
    
class MCLookbackCallOption(MCStockOption):
    """Inherits from the base class MCStockOption."""
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def __repr__(self):
        return (f'MCLookbackCallOption, s={self.s:.2f}, x={self.x:.2f}, t={self.t:.2f}, '
                f'r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, '
                f'num_trials={self.num_trials}')

    def value(self):
        self.values = []
        for _ in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            max_stock_price = np.max(stock_values)
            payoff = max(max_stock_price - self.x, 0)
            self.values.append(payoff)
        value = np.exp(-self.r * self.t) * np.mean(self.values)
        return value

    def stderr(self):
        sample_std = np.std(self.values)
        return sample_std / np.sqrt(self.num_trials)
    
class MCLookbackPutOption(MCStockOption):
    """Inherits from the base class MCStockOption."""
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        super().__init__(s, x, t, r, sigma, nper_per_year, num_trials)

    def __repr__(self):
        return (f'MCLookbackPutOption, s={self.s:.2f}, x={self.x:.2f}, t={self.t:.2f}, '
                f'r={self.r:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, '
                f'num_trials={self.num_trials}')

    def value(self):
        self.values = []
        for _ in range(self.num_trials):
            stock_values = self.generate_simulated_stock_values()
            min_stock_price = np.min(stock_values)
            payoff = max(self.x - min_stock_price, 0)
            self.values.append(payoff)
        value = np.exp(-self.r * self.t) * np.mean(self.values)
        return value

    def stderr(self):
        sample_std = np.std(self.values)
        return sample_std / np.sqrt(self.num_trials)
    
if __name__ == '__main__':
    ##test for __repr__ method
    option = MCStockOption(90, 100, 1.0, 0.1, 0.3, 250, 10)
    print(option)
    
    ##test for value(self) method
    option = MCStockOption(90, 100, 1.0, 0.1, 0.3, 250, 10)
    option.value()
    
    ##test for class MCEuroCallOption
    call = MCEuroCallOption(90, 100, 1, 0.1, 0.3, 100, 1000)
    print(call)
    call.value()
    call.value()
    call.stderr()
    
    call = MCEuroCallOption(90, 100, 1.0, 0.1, 0.3, 100, 1000)
    print(call)
    call.value()
    call.stderr()
    # change num_trials from 1,000 to 100,000
    call.num_trials = 100000
    call.value() # note: this took about 8 seconds to run on my computer
    call.stderr()
    
    call = MCEuroCallOption(40, 40, 0.25, 0.08, 0.30, 100, 100000)
    print(call)
    call.value()
    call.stderr()
    
    ##test for class MCEuroPutOption
    put = MCEuroPutOption(100, 100, 1.0, 0.1, 0.3, 100, 1000)
    print(put)
    put.value()
    put.value()
    put.value()
    put.value()
    put.value()
    
    put.stderr()
    
    ##test for class MCAsianCallOption
    acall = MCAsianCallOption(100, 100, 1.0, 0.10, 0.30, 100, 1000)
    print(acall)
    acall.value()
    acall.stderr()
    # change num_trials to reduce the standard error:
    acall.num_trials = 100000
    acall.value()
    acall.stderr()

    acall = MCAsianCallOption(35, 30, 1.0, 0.08, 0.25, 100, 100000)
    acall.value()
    acall.stderr()

    acall = MCAsianCallOption(35, 40, 1.0, 0.08, 0.40, 100, 100000)
    acall.value()
    acall.stderr()
    
    ##test for class MCAsianPutOption
    aput = MCAsianPutOption(100, 100, 1.0, 0.10, 0.30, 100, 1000)
    print(aput)
    aput.value()
    aput.stderr()
    
    # change num_trials to reduce the standard error:
    aput.num_trials = 100000
    aput.value()
    aput.stderr()
    
    aput = MCAsianPutOption(35, 30, 1.0, 0.08, 0.25, 100, 100000)
    aput.value()
    aput.stderr()
    
    aput = MCAsianPutOption(35, 40, 1.0, 0.08, 0.40, 100, 100000)
    aput.value()
    aput.stderr()
    
    ##test for class MCLookbackCallOption
    lcall = MCLookbackCallOption(100, 100, 1.0, 0.10, 0.30, 100, 1000)
    print(lcall)
    lcall.value()
    lcall.stderr()
    
    # change num_trials to reduce the standard error:
    lcall.num_trials = 100000
    lcall.value()
    lcall.stderr()
    
    lcall = MCLookbackCallOption(35, 30, 1.0, 0.08, 0.25, 100, 100000)
    lcall.value()
    lcall.stderr()
    
    lcall = MCLookbackCallOption(35, 40, 1.0, 0.08, 0.40, 100, 100000)
    lcall.value()
    lcall.stderr()
    
    ##test for class MCLookbackPutOption
    lput = MCLookbackPutOption(100, 100, 1.0, 0.10, 0.30, 100, 1000)
    print(lput)
    lput.value()
    lput.stderr()
    
    # change num_trials to reduce the standard error:
    lput.num_trials = 100000
    lput.value()
    put.stderr()
    
    lput = MCLookbackPutOption(35, 30, 1.0, 0.08, 0.25, 100, 100000)
    lput.value()
    lput.stderr()
    
    lput = MCLookbackPutOption(35, 40, 1.0, 0.08, 0.40,  100, 100000)
    lput.value()
    lput.stderr()

    
   












