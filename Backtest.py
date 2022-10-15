import utils

class Backtest:
    def __init__(self, tickers: list, start_date: str, end_date: str):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        curr_date = self.start_date

        while curr_date != self.end_date:
            for ticker in self.tickers:
                print(ticker.ticker_name, ticker.quantity)
            
            curr_date = utils.add_day(curr_date)    #Progress one day


