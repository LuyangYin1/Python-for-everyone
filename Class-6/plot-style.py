import datetime as dt 
import yfinance as yf
#import matplotlib as plt
import matplotlib.pyplot as plt


#yf.pdr_override()
start = dt.datetime(2024,1,1)
end = dt.datetime (2024,10,1)

df = yf.download('TSLA',start,end)
print(df['Adj Close'])
df['Adj Close'].plot(label="TSLA")
df_AAPL = yf.download('AAPL',start,end)
print(df_AAPL['Adj Close'])
df_AAPL['Adj Close'].plot(label="AAPL")
plt.title("comparing stock price")
plt.ylabel("price")
plt.legend(loc='upper left')
plt.show()

plt.bar()