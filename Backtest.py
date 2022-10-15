import utils
from typing import Callable

class Backtest:
    def __init__(self, tickers: list, start_date: str, end_date: str, evaluate_strategy: Callable):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.evaluate_strategy = evaluate_strategy #Strategy function

    def run(self):
        curr_date = self.start_date

        while curr_date != self.end_date:
            for ticker in self.tickers:
                self.evaluate_strategy(ticker.ticker_name)
            
            print(curr_date)
            curr_date = utils.add_day(curr_date)    #Progress one day


