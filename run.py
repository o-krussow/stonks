import random
import Ticker
import Backtest


def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]


nasdaq_tickers = read_tickers_from_file("nasdaq_tickers.txt")
objectified_nasdaq_tickers = [Ticker.Ticker(ticker_name, random.randint(0, 10)) for ticker_name in nasdaq_tickers]

bt = Backtest.Backtest(objectified_nasdaq_tickers, "2022-01-01", "2022-01-31")

bt.run()





