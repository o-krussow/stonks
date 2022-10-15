import yfinance as yf  
import matplotlib.pyplot as plt
import sys

def highest_percent_up(eod_prices):
    #this does not work 100% right now
    max_increase = sys.maxsize*-1
    top_5 = []

    num_days = len(eod_prices)
    for price_index in range(num_days):
        if eod_prices[price_index+1] / eod_prices[price_index] > max_increase:
            max_increase = eod_prices[price_index+1] / eod_prices[price_index]
            print("Increase:", max_increase)
            print("Old price:", eod_prices[price_index])
            print("New price:", eod_prices[price_index+1])
            print("Index:", price_index)
        else:
            break








#Right now, this is only giving us an end of day price for every day, instead of different times of every day.
data = yf.download('SHLDQ','2017-01-01','2022-01-01')

#Converting pandas dataframe to a list because I don't know how to use pandas at all rn
#If we want to scale this better we will want to use pandas/numpy so whatever computer we run this on won't scream
data_to_list = data["Adj Close"].values.tolist()
rounded_list = [round(price, 4) for price in data_to_list] #rounding the list because we do not need 64 bit precision for where we're going
print(len(rounded_list))


highest_percent_up(rounded_list)

