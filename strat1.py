from Strat import *
import random

class ExampleStrat(Strat):  #Strategy1 inherits from Strategy

    def __init__(self):
        super().__init__()

    #owen is stupid
    def recombobulate(self):
        return random.choice(["buy", "sell", "hold"]), random.randint(0, 5)

    def passes_sniff_test(self, decision, quantity, price, capital, ticker_quant_in_possession):
        if decision == "buy":
            return (quantity * price) <= capital
        elif decision == "sell":
            return quantity <= ticker_quant_in_possession
        else:
            return True

    #Example of overriding a function in Strat
    def main_strategy(self, ticker, ticker_quant_in_possession, price, date, capital):
        decision, quantity = self.recombobulate()

        while (not self.passes_sniff_test(decision, quantity, price, capital, ticker_quant_in_possession)):
            decision, quantity = self.recombobulate()

        return (decision, quantity)
