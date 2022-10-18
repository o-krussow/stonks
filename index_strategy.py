from xml.dom import NAMESPACE_ERR
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#!!! This file is all python implemented and based, I am going to start a new one that is primarily panda and time series based
#General format for getting closed numbers in a list.
#Need to consider how to offset 

stock_full = yf.download("NVDA", "2022-10-1", interval="5m")
stock_adjclose = stock_full['Adj Close'].values.tolist()

#Nasdaq closes and such
nas_full = yf.download("^IXIC", "2022-10-1", interval="5m")
nas_adjclose = nas_full['Adj Close'].values.tolist()

#stole these from the web so they work :)
def covariance(x, y):
    # Finding the mean of the series x and y
    mean_x = sum(x)/float(len(x))
    mean_y = sum(y)/float(len(y))
    # Subtracting mean from the individual elements
    sub_x = [i - mean_x for i in x]
    sub_y = [i - mean_y for i in y]
    numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    denominator = len(x)-1
    cov = numerator/denominator
    return cov

def correlation(x, y):
    # Finding the mean of the series x and y
    mean_x = sum(x)/float(len(x))
    mean_y = sum(y)/float(len(y))
    # Subtracting mean from the individual elements
    sub_x = [i-mean_x for i in x]
    sub_y = [i-mean_y for i in y]
    # covariance for x and y
    numerator = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    # Standard Deviation of x and y
    std_deviation_x = sum([sub_x[i]**2.0 for i in range(len(sub_x))])
    std_deviation_y = sum([sub_y[i]**2.0 for i in range(len(sub_y))])
    # squaring by 0.5 to find the square root
    denominator = (std_deviation_x*std_deviation_y)**0.5 # short but equivalent to (std_deviation_x**0.5) * (std_deviation_y**0.5)
    cor = numerator/denominator
    return cor

#Owen's stuff
def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]

#list of Stock tickers
stocks = read_tickers_from_file("nasdaq_tickers.txt")

#Returns a sorted dictionary of inputted number of stocks sorted by their covariance to the nasdaq
def stock_corel_report(number_of_stocks):
    stock_dict = {}
    #Goes through x amount of stocks (currently 500) and makes a dictionary of "ticker" : covariance
    for stock in stocks[:number_of_stocks]:
        stock_full = yf.download(stock, "2022-1-1", interval="5m")
        stock_adjclose = stock_full['Adj Close'].values.tolist()
        try:
            cor = correlation(stock_adjclose, nas_adjclose)
            stock_dict[stock] = cor
        except:
            continue

    #Sorts the stock_dict in ascending order by covariance
    sorted_dict = sorted(stock_dict.items(), key=lambda x: x[1], reverse=True)

    return(sorted_dict)

#prints a scatterplot of %change of a stock and the nasdaq
def scatterplot(stock):
    stock_full = yf.download(stock, "2022-10-1", interval="5m")
    stock_adjclose = stock_full['Adj Close'].values.tolist()
    perc_change_stock = [ (x - stock_adjclose[x_ind+1]) / stock_adjclose[x_ind + 1] for (x_ind, x) in enumerate(stock_adjclose[:-2])]
    perc_change_nas = [ (x - nas_adjclose[x_ind+1]) / nas_adjclose[x_ind + 1] for (x_ind, x) in enumerate(nas_adjclose[:-2])]
    #Making a baby panda out of the info :)
    d = {stock: perc_change_stock, 'nasdaq': perc_change_nas }
    df = pd.DataFrame(data=d)
    ax = sns.scatterplot(x = stock, y = "nasdaq", data=df)
    plt.show()

#compares %change to price change correlations
def correlation_testing():
    print(correlation(stock_adjclose, nas_adjclose))
    perc_change_stock = [ (x - stock_adjclose[x_ind+1]) / stock_adjclose[x_ind + 1] for (x_ind, x) in enumerate(stock_adjclose[:-2])]
    perc_change_nas = [ (x - nas_adjclose[x_ind+1]) / nas_adjclose[x_ind + 1] for (x_ind, x) in enumerate(nas_adjclose[:-2])]
    print(correlation(perc_change_stock, perc_change_nas))

#implements manual 5-30 min lag both directions for a given stock
#takes ticker, prints a list of tuples with the fromat ("ticker delay", correlation)
def timing_test(stock):
    time_dict = {}
    stock_full = yf.download(stock, "2022-10-1", interval="5m")
    stock_adjclose = stock_full['Adj Close'].values.tolist()
    time_dict[stock + '0'] = correlation(stock_adjclose, nas_adjclose)
    #Timing with stock after index
    for x in range(1,7):
        time = str(x*5) 
        cor = correlation(stock_adjclose[x:], nas_adjclose[:-x])
        time_dict[stock + time] = cor
    
    #timing with stock before index
    for x in range(1,7):
        time = str(x*-5) 
        cor = correlation(stock_adjclose[:-x], nas_adjclose[x:])
        time_dict[stock + time] = cor

    sorted_dict = sorted(time_dict.items(), key=lambda x: x[1], reverse=True)
    return(sorted_dict)

#inputs a list of stocks into timing test and outputs a sorted list of tuples
def stock_and_time_test(list_of_stocks):
    result_list = []
    for stock in list_of_stocks:
        try:
            stock_result = timing_test(stock[0])
            for cor_tuple in stock_result:
                result_list.append(cor_tuple)
        except:
            continue
    result_list.sort(key=lambda x:x[1], reverse = True)

    return result_list

