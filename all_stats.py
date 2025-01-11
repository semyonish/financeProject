from bank_stats import BankStats
from stats import Portfolio
from useful_functions import rub_str


class AllStats:
    portfolio: Portfolio

    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio

    def print_info(self):
        print('Всего баланс: ', rub_str(self.portfolio.total + BankStats.balance()))
        print('Всего:        ', rub_str(self.portfolio.total + BankStats.deposit_sum()))