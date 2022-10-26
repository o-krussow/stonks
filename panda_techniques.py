import pandas as pd
from mdb_connect import mdb_connect
import seaborn as sns
import matplotlib.pyplot as plt

mdb = mdb_connect()

def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]

ticker_list = read_tickers_from_file('volatile_369.txt')
dirty_ticker_list = read_tickers_from_file('dirty_tickers.txt')
clean_ticker_list = [x for x in ticker_list if x not in dirty_ticker_list]

def percent_change(ticker_list):
    df = mdb.get_pandas(ticker_list, '2022-10-01', '2022-10-14')
    df_percent_change = df.pct_change()
    return df_percent_change

#ticker_list must contain NDAQ and ONE (1) other stock!!
def single_stock_lag_test(stock_ticker, index_ticker, percent_change = False):
    ticker_list = [stock_ticker, index_ticker]
    df = mdb.get_pandas(ticker_list, '2022-10-01', '2022-10-14')
    if percent_change == True:
        df = df.pct_change()
    for lag in range(-6,0):
        df[index_ticker + " | " + stock_ticker + " " + str(lag*-5) + "min"] = df[stock_ticker].shift(lag)
    full_lag_cor = df.corr("pearson")
    useable_lag_cor = full_lag_cor.get(index_ticker)
    useable_lag_cor.drop([index_ticker, stock_ticker], inplace=True)
    final_lag_cor = useable_lag_cor.sort_values(ascending=False)
    return final_lag_cor

def stock_list_lag_test(ticker_list, index_list = None, percent_change = False):
    lag_ds = pd.Series(dtype = 'float64')
    if index_list == None:
        index_list = ticker_list
    progress_check = 0
    for index in index_list:
        for ticker in ticker_list:
            if index in ticker or ticker in index:
                continue
            stock_lag = single_stock_lag_test(ticker, index, percent_change)
            lag_ds = pd.concat([lag_ds, stock_lag])
            lag_ds.sort_values(ascending=False, inplace=True)
        progress_check += 1
        print(str(progress_check) + " out of " + str(len(index_list)))
    return lag_ds


def volatility():
    volatility = percent_change(clean_ticker_list).abs().mean().sort_values(ascending=False)
    top_quartile_len = int(len(volatility) * .1)
    top_quartile = volatility[:top_quartile_len]
    print(top_quartile)
    for key in top_quartile.keys():
        print(key)

df = stock_list_lag_test(ticker_list, percent_change=True)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df[:100])

