import utils

class Backtest:
    def __init__(self, tickers: list, start_date: str, end_date: str, strategy):
        self.tickers = tickers
        self.capital = 100    #Capital is $ to buy assets, right?
        self.start_date = start_date
        self.end_date = end_date
        self.strategy = strategy #Strategy object
        self.tickers_in_possession = {}

        for ticker in self.tickers:
            self.tickers_in_possession[ticker] = 0
    
    def get_ticker_price_at_time(self, ticker, timestamp):
        #Need to figure out the best way to query database at a given time, shouldn't be too hard I think? with
        #SELECT * FROM <ticker table> WHERE timestamp LIKE <something>
        #5 is placeholder
        return 5

    def print_ticker_summary(self):
        for ticker in sorted(self.tickers_in_possession.keys()):
            quantity = self.tickers_in_possession[ticker]
            print(quantity, "of", ticker)

    def run(self):
        curr_date = self.start_date

        #ok curr_date is gonna need to increment on smaller levels than a day, thats for later owen to do.

        while curr_date != self.end_date:
            for ticker in self.tickers:
                #call the strategy to determine what to do next
                #Setup "return signals" so Backtest class can communicate with our strategy function on what it decides to do.
                #This Backtest class is going to have to keep track of our capital, our quantities of different stocks, etc.

                curr_ticker_price = self.get_ticker_price_at_time(ticker, curr_date)

                curr_ticker_quant_in_possession = self.tickers_in_possession[ticker]

                decision, quantity = self.strategy.main_strategy(ticker, curr_ticker_price, curr_ticker_quant_in_possession, curr_date, self.capital)


                #print(curr_date, decision, quantity)

                if decision == "hold":
                    #do nothing
                    continue

                elif decision == "buy":
                    if self.capital - (quantity * curr_ticker_price) < 0:
                        raise Exception("Strategy tried to buy more than it could afford, fix that logic in your strategy class.")
                    else:
                        self.capital -= (quantity * curr_ticker_price)
                        self.tickers_in_possession[ticker] += quantity

                elif decision == "sell":
                    self.tickers_in_possession[ticker] -= quantity
                    self.capital += (quantity * curr_ticker_price)
                
                else:
                    raise Exception("Strategy returned an invalid decision. The decision needs to be a string, being 'buy', 'sell', or 'hold'.")

            #fix pls
            curr_date = utils.add_day(curr_date)    #Progress one day
        
        print(self.capital)
        self.print_ticker_summary()