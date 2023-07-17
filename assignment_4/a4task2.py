# 
# a4task2.py - Assignment 4, Task 2
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Fun with recursion
# 
#

from a4task1 import *

# function collect_bids(filename)
def collect_bids(filename):
    """ This function will process the data file containing the bids
        input filename: a file's path
    """
    bids = []
    
    with open(filename) as file:
        # Discard the first line (header)
        header = file.readline()

        # Process the rest of the file
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespaces
            values = line.split(",")  # Split the line into values
            values = [float(x) for x in values]
            bids.append(values)  # Append the price to the list
    return bids

# function print_bids(bids) 
def print_bids(bids):
    """ This function will process the a of bids, and produce a beautifully
        formatted table of the bids
        input bids: a list of bids
    """
    result = "Bid ID          Bid Amount           Price\n"
    for bid in bids:
        bid_id, bid_amount, price = bid
        result += f'   {bid_id:<10.0f}  ${bid_amount:>10.0f}          ${price:>8.3f}\n'
    return result



def find_winning_bids(bids, total_offering_fv, c, n, m):
    """ processes a list of bids and determine which are successful in the auction.
    
        The parameters are:
        bids, where each bid is a sublist in the form of [bid_id, bid_amount, bid_price],
        total_offering_fv is the total amount of bonds being sold,
        c is the annualized coupon rate,
        n is the number of years to maturity for the bonds, and
        m is the number of coupon payments per year.
        
        input bids: a list of bids
        input c: any number between 0 and 1(float)
        input n: any number(int)
        input m: any number(int)
        input total_offering_fv: any number(int or float)
    """
    print("Here are all of the bids:")
    print(print_bids(bids))
    # sort the bids by bid_price in descending order
    bids.sort(key=lambda x: x[2], reverse=True)
    print("Here are all of the bids, sorted by price descending:")
    print(print_bids(bids))
    remaining_fv = total_offering_fv
    winning_bids = []
    winnum = 0
    for i in range(len(bids)):
        bid_id, bid_amount, bid_price = bids[i]
        if bid_amount <= remaining_fv:
            # if the bid amount is less than or equal to the remaining fv,
            # then the bid is successful and the entire amount is filled.
            winning_bids.append([bid_id, bid_amount, bid_price])
            remaining_fv -= bid_amount
            winnum += 1
        elif remaining_fv > 0:
            # if the bid amount is more than the remaining fv,
            # then the bid is partially filled and the remaining fv is filled.
            winning_bids.append([bid_id, remaining_fv, bid_price])
            remaining_fv = 0
            winnum += 1
        else:
            # if the remaining fv is 0, then the bid is unsuccessful and the amount filled is 0.
            winning_bids.append([bid_id, 0, bid_price])

    # calculate the auction’s clearing_price
    if winning_bids:
        clearing_price = winning_bids[-1][2]
    else:
        clearing_price = 0

    # calculate the yield to maturity
    ytm = bond_yield_to_maturity(100, c, n, m, clearing_price)

    # print out the table showing all bids and the amount sold to each bidder
    print("\nThe auction is for ${:.2f} of bonds.".format(total_offering_fv))
    print("\n{} bids were successful in the auction.".format(winnum))
    print("The auction clearing price was ${:.3f}, i.e., YTM is {:.6f} per year.".format(clearing_price, ytm))
    print("Here are the results for all bids:")
    print(print_bids(winning_bids))

    return winning_bids


if __name__ == '__main__':

    # sample test call for function collect_bids(filename)
    print("collect_bids ( '/Users/apple/Downloads/bond_bids.csv' ) returns\n", collect_bids ( '/Users/apple/Downloads/bond_bids.csv' ))

    
    # sample test call for print_bids(bids)
    bids = collect_bids('/Users/apple/Downloads/bond_bids.csv')
    print("print_bids(bids) returns\n", print_bids(bids))
    
    # read in the bids
    bids = collect_bids('/Users/apple/Downloads/bond_bids.csv')
    print("Here are all the bids:")
    print_bids(bids)
    print()

    # process the bids in an auction of $500,000 of 5-year 3% semi-annual coupon bonds
    processed_bids = find_winning_bids(bids, 500000, 0.03, 5, 2)
    # process the bids in an auction of $1,400,000 of 5-year 3.25% semi-annual coupon bonds
    processed_bids = find_winning_bids(bids, 1400000, 0.0325, 5, 2)




















