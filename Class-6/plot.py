import datetime as dt 
import yfinance as yf
import matplotlib.pyplot as plt


#yf.pdr_override()
start = dt.datetime(2024,1,1)
end = dt.datetime (2024,9,1)

df = yf.download('AAPL',start,end)
print(df['Adj Close'])
df['Adj Close'].plot()
plt.show
