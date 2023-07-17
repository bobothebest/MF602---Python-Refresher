# 
# a5task3.py - Assignment 5, Task 3
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

from a4task1 import discount_factors, bond_cashflows # bond functions
from a5task1 import *
from a5task2 import *
  
# function bond_price(fv, c, n, m, r)
def bond_price(fv, c, n, m, r):
    """ this function calculate and return the price of a bond. The parameters are: fv is the future (maturity) value of the bond;
        c is the annual coupon rate expressed as percentage per year;
        n is the number of years until maturity;
        m is the number of coupon payments per year;
        and r, the annualized yield to maturity of the bond

        input fv: any number(int or float)
        input c: any number between 0 and 1(float)
        input n: any number(int)
        input m: any number(int)
        input r: any number between -1 and 1(float)
    """
    # Calculate the bond's cashflows
    cashflows = bond_cashflows(fv, c, n, m)
    
    # Calculate the relevant discount factors
    discount_factors_list = discount_factors(r, n, m)
    
    # Convert the cashflows and discount factors to a 2D list (matrix)
    cashflows_matrix = [[cf] for cf in cashflows]
    cashflows_matrix = transpose(cashflows_matrix)
    discount_factors_matrix = [[df] for df in discount_factors_list]

    # Calculate the dot product of the cashflows and discount factors
    price_matrix = dot_product(cashflows_matrix, discount_factors_matrix)

    # Convert the result to a float and return it
    return price_matrix[0][0]

# function bootstrap(cashflows, prices)
def bootstrap(cashflows, prices):
    """ this function implement the bootstrap method. This function will take 
        parameters cashflows, which is a matrix (2-dimensional list) 
        containing the cashflows for some bonds, and prices which is a column 
        matrix (2-dimensional list) containing the prices of these bonds.

        input cashflows: a matrix (2-dimensional list) 
        input prices: a column matrix (2-dimensional list)
    """
    # Calculate the inverse of the cashflows matrix
    inverse_cashflows = inverse_matrix(cashflows)
    
    # Calculate the matrix of implied discount factors
    discount_factors = dot_product(inverse_cashflows, prices)
    
    return discount_factors

if __name__ == '__main__':

    # sample test call for bond_price(fv, c, n, m, r)
    bond_price(1000, 0.08, 5, 2, 0.08) # coupon bond at par
    bond_price(1000, 0.08, 5, 2, 0.09) # coupon bond at discount
    bond_price(1000, 0.00, 5, 2, 0.09) # zero-coupon bond
    
    # sample test call for bootstrap(cashflows, prices)
    CF = [[105,0,0],[6,106,0],[7,7,107]]
    P = [[99.5], [101.25], [100.35]]
    D = bootstrap(CF, P)
    print_matrix(CF, 'Bond Cashflows')
    print_matrix(P, 'Bond Prices')
    print_matrix(D, 'Implied Discount Factors') 
    D




