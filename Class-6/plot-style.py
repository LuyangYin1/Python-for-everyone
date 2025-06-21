# pip install yfinance --upgrade --no-cache-dir
# pip install matplotlib
# pip install numpy
# pip install pandas
# documentation webpage : https://yfinance-python.org/index.html
# https://pypi.org/project/yfinance/

import datetime as dt
import yfinance as yf

# import matplotlib as plt
import matplotlib.pyplot as plt


# yf.pdr_override()
start = dt.datetime(2025, 1, 1)
end = dt.datetime(2025, 3, 1)

df = yf.download("TSLA", start, end)
print(df["Close"])
df["Close"].plot(label="TSLA")
df_AAPL = yf.download("AAPL", start, end)
print(df_AAPL["Close"])
df_AAPL["Close"].plot(label="AAPL")
plt.title("comparing stock price")
plt.ylabel("price")
plt.legend(loc="upper left")
# plt.bar(df.index,df['Close'])
# plt.bar(df_AAPL.index,df_AAPL['Close'])
plt.show()
# plt.bar()
