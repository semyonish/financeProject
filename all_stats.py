from bank_stats import BankStats
from deposits import DepositAvailability
from stats import Portfolio
from useful_functions import rub_str


class AllStats:
    portfolio: Portfolio

    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio

    def print_info(self):
        print('Всего баланс быстро: ', rub_str(self.portfolio.total + BankStats.balance(DepositAvailability.FAST)))
        print('Всего баланс средне: ', rub_str(self.portfolio.total + BankStats.balance(DepositAvailability.USUAL)))
        print('Всего баланс:        ', rub_str(self.portfolio.total + BankStats.balance(DepositAvailability.SLOW)))
        print('Всего:               ', rub_str(self.portfolio.total + BankStats.deposit_sum(DepositAvailability.SLOW)))