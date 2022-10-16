import yfinance as yf  
import utils

class Ticker:
    def __init__(self, ticker_name, quantity):
        self.ticker_name = ticker_name
        self.quantity = quantity

    def get_days_prices(self, day):
        #From range day to day+1, get prices on hourly interval.
        #This will fail if one of the days is across a weekend/holiday where the market is closed.
        #Todo: Figure out an elegant way to handle errors if .download cannot get a day for ^^^ reason.
        next_day = utils.add_day(day)
        data = yf.download(self.ticker_name, day, next_day, interval="60m")
        return data

    def __str__(self):
        return ("Name:" + self.ticker_name + " Quant:" + str(self.quantity))



if __name__ == "__main__":
    aapl = Ticker("AAPL", 10)
    print(aapl.get_days_prices("2022-01-04"))

