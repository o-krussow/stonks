import yfinance as yf  
import datetime

class Ticker:
    def __init__(self, ticker_name, quantity):
        self.ticker_name = ticker_name
        self.quantity = quantity

    # Day is the best "resolution" we can get right now
    def get_days_prices(self, day):
        #From range day to day+1, get prices on hourly interval.
        #This will fail if one of the days is across a weekend/holiday where the market is closed.
        #Todo: Figure out an elegant way to handle errors if .download cannot get a day for ^^^ reason.
        next_day = self._add_day(day)
        data = yf.download(self.ticker_name, day, next_day, interval="60m")
        return data

    def _add_day(self, date):
        day_1 = datetime.datetime.strptime(date, "%Y-%m-%d")
        next_date = day_1 + datetime.timedelta(days=1)    #Hopefully this takes care of month years/leap years and stuff for us

        return next_date.strftime("%Y-%m-%d")   #Convert datetime object back into a string with format %Y-%m-%d




if __name__ == "__main__":
    aapl = Ticker("AAPL", 10)
    print(aapl.get_days_prices("2022-01-04"))

