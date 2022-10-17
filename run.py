import random
import Ticker
import Backtest


def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]

def determine_article_tone(writeup: str):
    #The hope/idea is to determine whether the opinion of an article (text passed to function as a string) on a stock is positive or negative. I am not sure the best way of doing this yet.
    #I believe the return value should be a float value which scales to how positive/negative the article was.
    return 0

def determine_yahoo_sentiment(ticker):
    #Go through all the news articles associated with a given ticker, and figure out if the overall tone is positive or negative.
    #The idea is to use determine_article_tone(writeup) for every article this function encounters, and to determine a final score from all the sub scores
    return 0

def buy_or_sell(ticker):
    #Given an undecided list of parameters, should we buy or sell this stock?
    #We can use a similar idea used in machine learning:
    # w(1, 2, 3, and 4) are "weights" associated with each subscore (1 thru 4 is completely arbitrary for this example, we could go 1 thru 50 and the idea is the same.)
    # The different subscores would be results from different sentiment determining functions, as well as different functions considering price data.
    # Maybe a better word for "subscore" in this scenario would be "indicator." For example, maybe our subscore1 = determine_yahoo_sentiment(<our stock>)
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
    return 0


#This is an example of how we can implement one of our strategies, this function is passed to Backtest to be run further down in this file.
#Things like determining price histories, market sentiment, etc, need to be done in this function. Backtest just iterates through the tickers and keeps track of how many of each one we have.
def strategy1(ticker, curr_date):
    print(ticker.get_days_prices("2022-01-05"))
    #print(ticker)



#nasdaq tickers only for now, for testing-----------
nasdaq_tickers = read_tickers_from_file("nasdaq_tickers.txt")
objectified_nasdaq_tickers = [Ticker.Ticker(ticker_name, random.randint(0, 100)) for ticker_name in nasdaq_tickers]  #Making a list of Ticker objects with a random quantity from the original list of ticker strings
#----------------------------------------------------

#Run the Backtest
#Backtest(<ticker object list>, <start date>, <end date>, <strategy function>)
#Right now, there is nothing happening in the Backtest function asides from printing out all the tickers/quantities.
bt = Backtest.Backtest(objectified_nasdaq_tickers, "2022-01-01", "2022-01-31", strategy1)

bt.run()





