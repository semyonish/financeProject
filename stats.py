from tinkoff.invest import PortfolioResponse

from instruments import Instruments
from useful_functions import quotation_int, money_value_int, rub_percent_str, rub_str, percent_str


class Portfolio:
    def __init__(self, portfolios: [PortfolioResponse]):
        self.positions = {}  # figi -> position
        self.counts = {}  # figi -> count

        self.total_shares = 0
        self.total_bonds = 0
        self.total_futures = 0
        self.total_etfs = 0
        self.total_currencies = 0
        self.total = 0

        for portfolio in portfolios:
            self.total_shares += money_value_int(portfolio.total_amount_shares)
            self.total_bonds += money_value_int(portfolio.total_amount_bonds)
            self.total_futures += money_value_int(portfolio.total_amount_futures)
            self.total_etfs += money_value_int(portfolio.total_amount_etf)
            self.total_currencies += money_value_int(portfolio.total_amount_currencies)
            self.total += money_value_int(portfolio.total_amount_portfolio)

            for position in portfolio.positions:
                figi = position.figi
                self.positions[figi] = position
                self.counts[figi] = self.counts.get(figi, 0) + quotation_int(position.quantity)

        self.sums = {}
        self.names = {}
        for figi in self.positions:
            instrument = Instruments.get(figi)
            self.names[figi] = instrument.name
            self.sums[figi] = self.counts[figi] * money_value_int(self.positions[figi].current_price)

        self.sums = dict(sorted(self.sums.items(), key=lambda item: item[1], reverse=True))

    def print_info(self):
        print('---------------------------------')
        print('Акции:     ', rub_percent_str(self.total_shares, self.total))
        print('Облигации: ', rub_percent_str(self.total_bonds, self.total))
        print('Фонды:     ', rub_percent_str(self.total_etfs, self.total))
        print('Фьючерсы:  ', rub_percent_str(self.total_futures, self.total))
        print('Валюта:    ', rub_percent_str(self.total_currencies, self.total))
        print('---------------------------------')
        print('Всего:     ', rub_str(self.total))
        print('---------------------------------')

    def print_positions(self):
        for figi in self.sums:
            print(f'{percent_str(self.sums[figi], self.total)} | {self.names[figi]} | {rub_str(self.sums[figi])}')
