import utils
import Backtest

import strat1

def read_tickers_from_file(filename):
    with open(filename, "r") as f:
        f_contents = f.read()
    return f_contents.split("\n")[:-1]


def main(tickers, start_date, end_date, strategy):

    bt = Backtest.Backtest(tickers, start_date, end_date, strategy)
    bt.run()


if __name__ == "__main__":
    tickers = read_tickers_from_file("nasdaq_tickers.txt")

    strategy = strat1.ExampleStrat()

    main(tickers, "2022-09-15", "2022-10-13", strategy)