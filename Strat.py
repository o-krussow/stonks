import yfinance as yf
import utils

#Think of this class as a "blueprint" for other strategies. Other strategies should inherit from this class, just so we can keep
#them mostly similar and predictable as we progress here.
class Strat:
    def __init__(self):
        self.watchlist = []

    def main_strategy(self, ticker, price, ticker_quant_in_possession, date, capital):
        #This function should return tuple (decision, quantity) where decision can be strings "buy", "sell", or "hold"
        #and quantity is quantity of the ticker to buy/sell

        #Given an undecided list of parameters, should we buy or sell this stock?
        #We can use a similar idea used in machine learning:
        # w(1, 2, 3, and 4) are "weights" associated with each subscore (1 thru 4 is completely arbitrary for this example, we could go 1 thru 50 and the idea is the same.)
        # The different subscores would be results from different sentiment determining functions, as well as different functions considering price data.
        # Maybe a better word for "subscore" in this scenario would be "indicator." For example, maybe our subscore1 = utils.determine_yahoo_sentiment(<our stock>)
        #   (w1) * (subscore1) + (w2) * (subscore2) + (w3) * (subscore3) + (w4) * (subscore4) = predetermined value for training
        #   where we adjust weights w(1, 2, 3, 4, ...) in the above function to try to equal a predetermined value, in order to make the best possible trade decision given the current subscores.
        # The more reference points we have, the more likely our weights will accurately represent the importance of each subscore.
        # Once the weights are determined to be a good fit, we can use them to determine if we should buy or sell in the future, given subscores.
        # Determining the weights is probably easier said than done.
        #
        # Something to think about: do we want this function to just tell us to buy or sell, or should we try to make it guess the price at a time interval? Or come up with some proprietary score?
        # The hope was to abstract away a bunch of buy/sell indicators behind a function, but I suppose different strategies will affect how this function is used big-ly.
        #
        # I'm sure there is a better way of doing this but this is sort of what makes sense to me in the moment.
        return ("hold", 0)
    
    def update_watchlist(self):
        #potentially we would keep a list of tickers that seem especially good with a given strategy, and we would update this list from time to time in order of
        #best response to worst response.
        return 0

