import utils
from typing import Callable

class Backtest:
    def __init__(self, tickers: list, start_date: str, end_date: str, evaluate_strategy: Callable):
        self.tickers = tickers
        self.capital = 0    #Capital is $ to buy assets, right?
        self.start_date = start_date
        self.end_date = end_date
        self.evaluate_strategy = evaluate_strategy #Strategy function

    def run(self):
        curr_date = self.start_date

        while curr_date != self.end_date:
            for ticker in self.tickers:
                #call the strategy to determine what to do next
                #Setup "return signals" so Backtest class can communicate with our strategy function on what it decides to do.
                #This Backtest class is going to have to keep track of our capital, our quantities of different stocks, etc.
                self.evaluate_strategy(ticker, curr_date)
            
            print(curr_date)
            curr_date = utils.add_day(curr_date)    #Progress one day
            