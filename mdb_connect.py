import mariadb
from datetime import datetime
import utils

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

if __name__ == "__main__":
    mdb = mdb_connect()
    print(mdb.get_prices("NVDA", "2022-9-10", "2022-10-12"))