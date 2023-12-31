## Main Ideas
We are looking for strategies, not stocks (to an extent)

Figure out when gains are realized for tax purposes

Use google trends

Consider weekends in trading, big spikes happen a lot here it seems

What data do we need? Just closing prices for a given interval, or do we want all of the information given by yfinance?

## Lets say we have a stock ticker, determine name of company from the stock ticker
- Now check google trends for the name of the company as the key word
- Check news page on google and find which words pop up a lot, use beautiful soup to scrape
- It would be nice if somehow we could determine positive or negative sentiment from this result

## Strategies:
- Find stock that follows some index fund roughly, and if stock does not follow index fund when index fund goes up, buy because it probably will. (Same idea if going down)

- Find best "sell level" (or % up) per stock based on back testing, figure out same for downwards trends, determine where to cut losses.

- It would be good if we could cache all our data so we don't have to slam yahoo servers every time we want to run a backtest.
 - Maybe I could set up nginx/dns server to take care of this.
 - Alternatively, we download all the data into some sort of CSV/JSON/some other kind of database thing and query it from there.

I have decided that I would like to fit all the pricing data we can get our grubby little hands on in a MariaDB or Postgres database. This way, we have a centralized location that we can (very rapidly!) query for data.

## Useful links:

Determining public sentiment: https://monkeylearn.com/blog/sentiment-analysis-machine-learning/






