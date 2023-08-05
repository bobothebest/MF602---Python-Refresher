# 
# a10task1.py - Assignment 10, Task 1
# Name:Ziyuan Zhang
# Email address:xiguifei@bu.edu
# Description: Writing SQL Queries
# 
#

import sqlite3 as db
import pandas as pd


# These queries will help you discover the database schema (structure).

example_0a = '''SELECT name FROM sqlite_master'''
example_0b = '''pragma table_info(clients)'''
example_0c = '''pragma table_info(trades)'''
example_0d = '''pragma table_info(price_history)'''


# This is an example query that you can use to get started:
## QUERY 00 SHOW ALL CLIENTS IN DATABASE
sql_00 = '''
SELECT * 
FROM clients
'''

sql_01 = """
SELECT * 
FROM price_history 
WHERE date = '2020-12-31' 
ORDER BY security;
"""

sql_02 = """
SELECT * 
FROM trades 
WHERE client_id = 4 
ORDER BY trade_date;
"""

sql_03 = """
SELECT * 
FROM trades 
WHERE trade_date >= '2018-01-01' AND trade_date <= '2018-12-31' 
ORDER BY trade_date;
"""

sql_04 = """
SELECT security, COUNT(*) AS number_of_trades 
FROM trades 
GROUP BY security 
ORDER BY security;
"""

sql_05 = """
SELECT clients.first_name, clients.last_name, COUNT(trades.trade_id) AS number_of_trades 
FROM clients 
INNER JOIN trades ON clients.client_id = trades.client_id 
GROUP BY clients.first_name, clients.last_name 
ORDER BY number_of_trades DESC;
"""

sql_06 = """
SELECT trades.trade_date, trades.quantity, clients.first_name, clients.last_name 
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id 
WHERE trades.security = 'CSCO' 
ORDER BY trades.trade_date;
"""

sql_07 = """
SELECT trades.trade_date, clients.first_name, clients.last_name, trades.security, trades.quantity 
FROM trades 
INNER JOIN clients ON trades.client_id = clients.client_id 
WHERE trades.trade_date >= '2019-01-01' AND trades.trade_date <= '2019-12-31' 
ORDER BY trades.trade_date;
"""

sql_08 = """
SELECT trades.trade_date, trades.security, trades.quantity, price_history.price AS price
FROM trades
INNER JOIN clients ON trades.client_id = clients.client_id
INNER JOIN price_history ON trades.trade_date = price_history.date AND trades.security = price_history.security
WHERE clients.first_name = 'Angela' AND clients.last_name = 'Merkel'
ORDER BY trades.trade_date;
"""

sql_09 = """
SELECT trades.security, 
       SUM(trades.quantity) AS quantity, 
       price_history.price AS price, 
       SUM(trades.quantity) * price_history.price AS value
FROM trades
INNER JOIN clients ON trades.client_id = clients.client_id
INNER JOIN price_history ON trades.security = price_history.security
WHERE clients.first_name = 'Angela' 
      AND clients.last_name = 'Merkel' 
      AND price_history.date = '2020-12-31'
GROUP BY trades.security
ORDER BY value DESC;
"""

sql_10 = """
SELECT trades.trade_date, 
       trades.security, 
       trades.quantity, 
       purchase_price.price AS purch_price, 
       trades.quantity * purchase_price.price AS cost, 
       current_price.price AS current_price, 
       trades.quantity * current_price.price AS value
FROM trades
INNER JOIN clients ON trades.client_id = clients.client_id
INNER JOIN price_history AS purchase_price ON trades.security = purchase_price.security AND trades.trade_date = purchase_price.date
INNER JOIN price_history AS current_price ON trades.security = current_price.security AND current_price.date = '2020-12-30'
WHERE clients.first_name = 'Angela' 
      AND clients.last_name = 'Merkel'
ORDER BY trades.security ASC, trades.trade_date ASC;
"""
################################################################################
if __name__ == '__main__':
    
    # obtain a database connection:
    con=db.connect("/Users/apple/Downloads/portfolio.db")
    
    # set some options to display enough columns of output
    pd.set_option('display.width', 320)
    pd.set_option('display.max_columns',10)
    
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    print(pd.read_sql(example_0b, con=con))
    print()
    
    # Ask Pandas to run a query and return the resulting data set as a pd.DataFrame object:
    print(pd.read_sql(sql_00, con=con))
    print()      
    
    # Ask Pandas to run a query and retrieve all records from the price_history table for the date of 2020-12-31, in order by security
    print(pd.read_sql(sql_01, con=con))
    print()  
    
    print(pd.read_sql(sql_02, con=con))
    print() 
    
    print(pd.read_sql(sql_03, con=con))
    print() 
    
    print(pd.read_sql(sql_04, con=con))
    print() 
    
    print(pd.read_sql(sql_05, con=con))
    print() 
    
    print(pd.read_sql(sql_06, con=con))
    print() 

    print(pd.read_sql(sql_07, con=con))
    print() 
    
    print(pd.read_sql(sql_08, con=con))
    print() 
    
    print(pd.read_sql(sql_09, con=con))
    print() 
    
    print(pd.read_sql(sql_10, con=con))
    print() 
