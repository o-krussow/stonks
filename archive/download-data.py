import yfinance as yf

#Getting price data from October 1st 2022 to current in interval of 5minutes
#5m interval only lets us go 60 days back, I guess that's the extent of what yahoo stores for a stock.
data = yf.download("AAPL", "2022-9-01", interval="5m")
print(data)

#More interesting information:
#Maybe some of the information returned by different yf.Ticker() functions would make it easier for us to determine market sentiment without using google.
aapl = yf.Ticker("AAPL")
print(aapl.info)