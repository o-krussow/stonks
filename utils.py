#Put functions that multiple files use in here

import datetime

def add_day(date):
    day_1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    next_date = day_1 + datetime.timedelta(days=1)    #Hopefully this takes care of month years/leap years and stuff for us

    return next_date.strftime("%Y-%m-%d")   #Convert datetime object back into a string with format %Y-%m-%d


#For use in strategy classes
def determine_article_tone(writeup: str):
    #The hope/idea is to determine whether the opinion of an article (text passed to function as a string) on a stock is positive or negative. I am not sure the best way of doing this yet.
    #I believe the return value should be a float value which scales to how positive/negative the article was.
    return 0

def determine_yahoo_sentiment(ticker):
    #Go through all the news articles associated with a given ticker, and figure out if the overall tone is positive or negative.
    #The idea is to use determine_article_tone(writeup) for every article this function encounters, and to determine a final score from all the sub scores
    return 0