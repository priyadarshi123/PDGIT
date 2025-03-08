import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use("seaborn")
symbol = "AAPL"
df=yf.download(tickers = symbol)
print(df.index)
df.info()
print(df)
df.Close.plot(figsize = (12,8), fontsize = 12)
plt.ylabel('Price(USD)')
plt.title("Price chart")
plt.show()


