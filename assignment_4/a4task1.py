# 
# a4task1.py - Assignment 4, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

# function cashflow_times(n, m)
def cashflow_times(n, m):
    """ this function develops the list of the times at which a bond makes 
        coupon payments, with n years and m coupon payments per year.
        input n: any number(int)
        input m: any number(int)
    """
    lis = list(range(1, n*m+1))
    return lis

# function discount_factors(r, n, m)
def discount_factors(r, n, m):
    """ this function calculates and returns a list of discount factors for a 
        given annualized interest rate r, for n years, and m discounting 
        periods per year.
        input r: any number between 0 and 1(float)
        input n: any number(int)
        input m: any number(int)
    """
    return [1 / (1 + r/m)**(i) for i in range(1, n*m+1)]

# function bond_cashflows(fv, c, n, m)
def bond_cashflows(fv, c, n, m):
    """ this function calculate and return a list of cashflows for a bond 
        specified by the parameters. The parameters are: fv is the future 
        (maturity) value of the bond;
        c is the annual coupon rate expressed as percentage per year;
        n is the number of years until maturity;
        m is the number of coupon payments per year.
        
        input fv: any number(int or float)
        input c: any number between 0 and 1(float)
        input n: any number(int)
        input m: any number(int)
    """
    cou = [c/m * fv for x in cashflow_times(n, m)]
    cou[-1] += fv
    return cou

# function bond_price(fv, c, n, m, r) 
def bond_price(fv, c, n, m, r) :
    """ this function calculate and return the price of a bond. 
        The parameters are: fv is the future (maturity) value of the bond;
        c is the annual coupon rate expressed as percentage per year;
        n is the number of years until maturity;
        m is the number of coupon payments per year;
        and r, the annualized yield to maturity of the bond
 
        input c: any number between 0 and 1(float)
        input n: any number(int)
        input m: any number(int)
        input r: any number(int or float)
    """
    cashflows = bond_cashflows(fv, c, n, m)
    discount_factors_list = discount_factors(r, n, m)
    pv = sum([x*y for x,y in zip(cashflows, discount_factors_list)])
    return pv

# function bond_yield_to_maturity(fv, c, n, m, price) 
def bond_yield_to_maturity(fv, c, n, m, price):
    """ calculate the annualized yield_to_maturity on a bond. 
        The parameters are: fv is the future (maturity) value of the bond;
        c is the annual coupon rate expressed as percentage per year;
        n is the number of years until maturity;
        m is the number of coupon payments per year;
        and price is the current market price of the bond

        input fv: any number(int or float)
        input c: any number between 0 and 1(float)
        input n: any number(int)
        input m: any number(int)
        input price: any number(int or float)
    """
    r_low  = -1
    r_high = 1
    ACCURACY = 0.0001
    r = (r_low + r_high)/2
    diff = price - bond_price(fv, c, n, m, r)
    while abs(diff) > ACCURACY:
        if diff > 0:
            r_high = r
            r = (r_low + r_high)/2
        else:
            r_low = r
            r = (r_low + r_high)/2
        diff = price - bond_price(fv, c, n, m, r)
    return r

if __name__ == '__main__':

    # sample test call for function cashflow_times(n, m)
    # 5-year bond with 2 coupons/year
    print('cashflow_times(5,2) returns', cashflow_times(5,2))
    # 3-year bond with 4 coupons/year
    print('cashflow_times(3,4) returns', cashflow_times(3,4))
    # 2-year bond with monthly coupons
    print('cashflow_times(2,12) returns', cashflow_times(2,12))
    
    # sample test call for discount_factors(r, n, m)
    # 3% rate, 1 years, 2 payments/year
    print('discount_factors(0.03, 1, 2) returns', discount_factors(0.03, 1, 2))
    # 5% rate, 5 years, 2 payments/year
    print('discount_factors(0.05, 5, 2) returns', discount_factors(0.05, 5, 2))

    # sample test call for bond_cashflows(fv, c, n, m)
    # 5 year bond with 2 coupons/year
    print('bond_cashflows(1000, 0.08, 5, 2) returns', bond_cashflows(1000, 0.08, 5, 2))
    # 2 year bond with 2 coupons/year
    print('bond_cashflows(10000, 0.0575, 2, 2) returns', bond_cashflows(10000, 0.0575, 2, 2))
    # 2 year bond with 4 coupons/year
    print('bond_cashflows(5000, 0.09, 2, 4) returns', bond_cashflows(5000, 0.09, 2, 4))

    # sample test call for bond_price(fv, c, n, m, r) 
    # 3-year, 4% coupon bond, semi-annual coupons, priced at 4% annualized YTM.
    print('bond_price(100, 0.04, 3, 2, 0.04)  returns', bond_price(100, 0.04, 3, 2, 0.04))
    # 3-year, 4% coupon bond, semi-annual coupons, priced at 3% annualized YTM.
    print('bond_price(100, 0.04, 3, 2, 0.03)  returns', bond_price(100, 0.04, 3, 2, 0.03))
    # 3-year, 4% coupon bond, semi-annual coupons, priced at 5% annualized YTM.
    print('bond_price(100, 0.04, 3, 2, 0.05)   returns', bond_price(100, 0.04, 3, 2, 0.05))

    # sample test call for function bond_yield_to_maturity(fv, c, n, m, price)
    print('bond_yield_to_maturity(100, 0.04, 3, 2, 101.75) returns', bond_yield_to_maturity(100, 0.04, 3, 2, 101.75))
    # annuity payment for pv of $27,667 for 60 months at 0.9% APR
    print('bond_yield_to_maturity(1000, 0.08, 5, 1, 950) returns', bond_yield_to_maturity(1000, 0.08, 5, 1, 950))

    







