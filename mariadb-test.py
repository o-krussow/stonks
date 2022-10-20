import sys
import mariadb
import utils
import yfinance as yf
import pandas as pd


def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]

#I would be very sad if this function was run accidently so pls dont
def drop_tables():
    f_contents = read_tickers_from_file("nasdaq_tickers.txt")

    #for ticker in f_contents:
    #    cursor.execute("DROP TABLE "+ticker+";")

def build_tables():
    #f_contents = read_tickers_from_file("nasdaq_tickers.txt")

    #f_contents = ["^IXIC", "^DJI", "^GSPC", "^TYX"]

    for ticker in f_contents:
        try:
            cursor.execute("CREATE TABLE "+ticker+"( timestamp varchar(30), price FLOAT, primary key(timestamp));")

            print(ticker)

            data = yf.download(ticker, "2022-08-21", "2022-10-17", interval="5m")["Adj Close"].to_dict()
            new_data = {}
            #Converts this nonsense: Timestamp('2022-10-13 15:50:00-0400', tz='America/New_York') to 2022-10-13
            for timestamp in data.keys():
                new_data[str(pd.to_datetime(timestamp))] = data[timestamp]

            for key in sorted(new_data.keys()):
                cursor.execute("INSERT INTO "+ticker+" (timestamp, price) VALUES (\""+key+"\", "+str(new_data[key])+");")

        except mariadb.OperationalError:
            continue
        except mariadb.ProgrammingError:
            continue

        
    


if __name__ == "__main__":

    con = mariadb.connect(
        user = "user",
        password = "password1",
        host = "192.168.1.168",
        port = 3306,
        database="stonks"
    )

    cursor = con.cursor()


    ###drop_tables()
    build_tables()




