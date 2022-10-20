import pandas as pd
from mdb_connect import mdb_connect

mdb = mdb_connect()
ticker_list = ["NDAQ", "AAPL", "MSFT", "GOOG", "NFLX"]
df = mdb.get_pandas(ticker_list, '2022-10-1', '2022-10-14')

print(df.corr())
