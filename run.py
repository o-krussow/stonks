import random
import Ticker
import Backtest


def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]


#This is an example of how we can implement one of our strategies, this function is passed to Backtest to be run further down in this file.
#Things like determining price histories, market sentiment, etc, need to be done in this function. Backtest just iterates through the tickers and keeps track of how many of each one we have.
def strategy1(ticker_name, quantity, curr_date):
    print(ticker_name, quantity)


#nasdaq tickers only for now, for testing-----------
nasdaq_tickers = read_tickers_from_file("nasdaq_tickers.txt")
objectified_nasdaq_tickers = [Ticker.Ticker(ticker_name, random.randint(0, 100)) for ticker_name in nasdaq_tickers]  #Making a list of Ticker objects with a random quantity from the original list of ticker strings
#----------------------------------------------------

#Run the Backtest
#Backtest(<ticker object list>, <start date>, <end date>, <strategy function>)
#Right now, there is nothing happening in the Backtest function asides from printing out all the tickers/quantities.
bt = Backtest.Backtest(objectified_nasdaq_tickers, "2022-01-01", "2022-01-31", strategy1)

bt.run()





