"""
Financial Data Analysis with Python

This module demonstrates how to work with financial data using Python libraries:
- yfinance: Downloading stock market data from Yahoo Finance
- pandas: Data manipulation and analysis
- matplotlib: Data visualization
- openpyxl: Excel file operations

The module covers:
- Data acquisition from Yahoo Finance
- Portfolio data management
- Excel file operations
- Basic stock price visualization
- Multi-stock comparison

Prerequisites:
    pip install yfinance --upgrade --no-cache-dir
    pip install matplotlib
    pip install numpy
    pip install pandas
    pip install openpyxl

Author: Avnit
Date: 2024
"""

import pandas as pd
import datetime as dt 
import yfinance as yf
import matplotlib.pyplot as plt
import math
#  import price
data = pd.read_excel('apple.xlsx')
print(data.head(5))

data.to_excel('apple2.xlsx')

start = dt.datetime(2025,1,1)
end = dt.datetime (2025,4,1)

df = yf.download('AAPL',start,end)
print(df.head(5))

initial_portfolio = ['AAPL','GOOG','SPY','MSFT','TSLA']
df_portfolio = yf.download(initial_portfolio,start,end)
print(df_portfolio.head(5))

#pip install openpyxl
df.to_excel('apple2.xlsx')
df_portfolio.to_excel('myportfolio.xlsx')

# To get closing pricing for APPL on a specific date 
#print(df['Adj Close']['2024-01-08'])

print((df_portfolio['Close']['GOOG']['2025-02-07']))
print((df_portfolio['Close']['AAPL']['2025-02-07']))

#plt.plot(df['Close'])
plt.plot(df_portfolio['Close']['AAPL'],label='AAPL') 
plt.plot(df_portfolio['Close']['GOOG'],label='GOOG')
plt.plot(df_portfolio['Close']['SPY'],label='SPY')
plt.plot(df_portfolio['Close']['MSFT'],label='MSFT')
plt.plot(df_portfolio['Close']['TSLA'],label='TSLA')
plt.title('Stock Prices')
plt.xlabel('Date')
plt.legend()
plt.show()