import datetime as dt 
import yfinance as yf

#yf.pdr_override()
start = dt.datetime(2024,1,1)
end = dt.datetime (2024,9,1)

df = yf.download('AAPL',start,end)
print(df.head(5))

initial_portfolio = ['AAPL','GOOG','SPY','MSFT','TSLA']
df_portfolio = yf.download(initial_portfolio,start,end)
print(df_portfolio.head(5))

# pip install openpyxl
#df.to_excel('apple.xlsx')
#df.to_excel('myportfolio.xlsx')

# To get closing pricing for APPL on a specific date 
print(df['Adj Close']['2024-01-08'])
print((df_portfolio['Adj Close']['AAPL']['2024-02-08']))