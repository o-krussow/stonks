import mariadb
from datetime import datetime
import utils
import pandas as pd

class mdb_connect():
    def __init__(self, hostname="192.168.1.168", db="stonks", username="user", password="password1"):
        self.con = mariadb.connect(
            user = username,
            password = password,
            host = hostname,
            port = 3306,
            database=db
        )
        self.cursor = self.con.cursor()


    def get_prices(self, ticker, start_date, end_date=datetime.strftime(datetime.now(), "%Y-%m-%d")):
        curr_day = start_date

        return_dict = {}

        while curr_day != utils.add_day(end_date):

            self.cursor.execute("SELECT * FROM "+ticker+" WHERE timestamp LIKE \"%"+curr_day+"%\";")
            for (date, price) in self.cursor:
                return_dict[date] = price

            curr_day = utils.add_day(curr_day)
        
        return return_dict

    def get_pandas(self, ticker_list, start_date, end_date=datetime.strftime(datetime.now(), "%Y-%m-%d")):
        data_dict = {}
        time_set = set()
        panda_input = {}
        for ticker in ticker_list:
            x = self.get_prices(ticker, start_date, end_date)
            time_set.update(x.keys())
        for ticker in ticker_list:
            x = self.get_prices(ticker, start_date, end_date)
            for time in time_set:
                if time not in x.keys():
                    x[time] = None
            data_dict[ticker] = sorted(x.items())
            price_list = []
            for item in data_dict[ticker]:
                price_list.append(item[1])
            panda_input[ticker] = price_list
       
        df = pd.DataFrame(panda_input, index=x.keys())
        return df

if __name__ == "__main__":
    mdb = mdb_connect()
    print(mdb.get_prices("NDAQ", "2022-9-10", "2022-10-12"))
