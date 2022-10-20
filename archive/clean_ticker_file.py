import mariadb

def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]


def get_prices(ticker, cursor):
    return_dict = {}

    try:
        cursor.execute("SELECT * FROM "+ticker+";")
        if list(cursor) == []:
            return(True)    
        #return_dict[date] = price

    except mariadb.ProgrammingError:
        return(True)
        

    
    #return return_dict

tickers = read_tickers_from_file("nasdaq_tickers.txt")

con = mariadb.connect(
    user = "user",
    password = "password1",
    host = "192.168.1.168",
    port = 3306,
    database="stonks"
)

cursor  = con.cursor()

bad_tickers = []

for ticker in tickers:
    if get_prices(ticker, cursor):
        bad_tickers.append(ticker)

for ticker in bad_tickers:
    tickers.remove(ticker)

with open("cleaned_nasdaq_tickers.txt", "w+") as f:
    for ticker in tickers:
        f.write(ticker+"\n")

