# 
# a1task3.py - Assignment 1, Task 3
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Functions for time value of money calculations
# 
#

# function fv_lump_sum
def fv_lump_sum(r, n, pv):
    """ returns the future value of a lump sump pv invested at the periodic 
        rate r for n periods
        input r: any number between 0 and 1(float)
        input n: any  positive number(int)
        input pv: any number(int or float)
    """
    return pv * (1 + r) ** n

# function pv_lump_sum(r, n, fv)
def pv_lump_sum(r, n, fv):
    """ returns the present value of a lump sum fv to be received in the future,
        discounted at the periodic rate r for n periods.
        input r: any number between 0 and 1(float)
        input n: any  positive number(int)
        input fv: any number(int or float)
    """
    return fv / ((1 + r) ** n)

# function fv_annuity(r, n, pmt)
def fv_annuity(r, n, pmt):
    """ returns the future value of an annuity of pmt to be received each period
        for n periods, invested at the periodic rate r.
        input r: any number between 0 and 1(float)
        input n: any  positive number(int)
        input pmt: any number(int or float)
    """
    return pmt * ((1 + r) ** n - 1) / r

# function pv_annuity(r, n, pmt)
def pv_annuity(r, n, pmt):
    """ returns the present value of an annuity of pmt to be received each period
        for n periods, discounted at the rate r.
        input r: any number between 0 and 1(float)
        input n: any  positive number(int)
        input pmt: any number(int or float)
    """
    return pmt * (1 - (1 + r) ** (-n)) / r

# function annuity_payment(r, n, pv)
def annuity_payment(r, n, pv):
    """ returns the annuity payment for a present value of pv to be repaid at a periodic interest rate of r for n periods
        input r: any number between 0 and 1(float)
        input n: any  positive number(int)
        input pv: any number(int or float)
    """
    return r * pv / (1 - (1 + r) ** (-n))

# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':

    # sample test call for function fv_lump_sum
    # $100 at 5% rate for 2 years
    print('fv_lump_sum(0.05, 2, 100) returns', fv_lump_sum(0.05, 2, 100))
    # $400 at 8% APR for 20 years (with monthly compounding)
    print('fv_lump_sum(0.08/12, 20*12, 400) returns', fv_lump_sum(0.08/12, 20*12, 400))

    # sample test call for function pv_lump_sum
    # $1000 to be received in 5 years at 6% per year
    print('pv_lump_sum(0.06, 5, 1000) returns', pv_lump_sum(0.06, 5, 1000))
    # $500 received in 5 years, 6% APR, semi-ann. compounding
    print('pv_lump_sum(0.06/2, 5*2, 500) returns', pv_lump_sum(0.06/2, 5*2, 500))

    # sample test call for function fv_annuity(r, n, pmt)
    # invest $100 per year for 5 years at 4% interest
    print('fv_annuity(0.04, 5, 100) returns', fv_annuity(0.04, 5, 100))
    # invest $100 per month for 10 years at 9% APR
    print('fv_annuity(0.09/12, 10*12, 100) returns', fv_annuity(0.09/12, 10*12, 100))

    # sample test call for function pv_annuity(r, n, pmt)
    # pv of 30 payments of $250 per year, 5% interest
    print('pv_annuity(0.05, 30, 250) returns', pv_annuity(0.05, 30, 250))
    # pv of 60 payments of $471.75 per month, 0.9% APR
    print('pv_annuity(0.009/12,60, 471.75) returns', pv_annuity(0.009/12,60, 471.75))

    # sample test call for function annuity_payment(r, n, pv)
    # # annuity payment for pv of $1,000 for 10 year at 5%
    print('annuity_payment(0.05, 10, 1000) returns', annuity_payment(0.05, 10, 1000))
    # annuity payment for pv of $27,667 for 60 months at 0.9% APR
    print('annuity_payment(0.009/12, 60, 27667.44) returns', annuity_payment(0.009/12, 60, 27667.44))

    
    
    
    
    
    
    
    
    
    
    
    