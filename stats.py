import pandas as pd
from tinkoff.invest import PortfolioResponse, InstrumentType

from instruments import Instruments, DOLLAR_FIGI, DOLLAR_CURRENCY
from useful_functions import quotation_float, money_value_float, rub_percent_str, rub_str, percent_str, float2f, \
    percent2f

FUTURES_X_1000_FIGIS_PREFIXES = [
    'FUTCNY',
    'FUTBR'
]

FUTURES_X_USD_FIGIS_PREFIXES = [
    'FUTSPY',
    'FUTNASD'
]

FUTURES_X_0_01_FIGIS_PREFIXES = [
    'FUTNASD'
]


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
            self.total_shares += money_value_float(portfolio.total_amount_shares)
            self.total_bonds += money_value_float(portfolio.total_amount_bonds)
            self.total_futures += abs(money_value_float(portfolio.total_amount_futures))
            self.total_etfs += money_value_float(portfolio.total_amount_etf)
            self.total_currencies += money_value_float(portfolio.total_amount_currencies)
            self.total += money_value_float(portfolio.total_amount_portfolio)

            for position in portfolio.positions:
                figi = position.figi
                self.positions[figi] = position
                self.counts[figi] = self.counts.get(figi, 0) + quotation_float(position.quantity)

        self.sums = {}
        self.names = {}
        for figi in self.positions:
            instrument = Instruments.get(figi)
            self.names[figi] = instrument.name
            self.sums[figi] = self.counts[figi] * money_value_float(self.positions[figi].current_price)
            if instrument.instrument_kind == InstrumentType.INSTRUMENT_TYPE_FUTURES:
                self.convert_futures_sum(figi)

        self.sums = dict(sorted(self.sums.items(), key=lambda item: item[1], reverse=True))

    def print_info(self):
        print('Акции:     ', rub_percent_str(self.total_shares, self.total))
        print('Облигации: ', rub_percent_str(self.total_bonds, self.total))
        print('Фонды:     ', rub_percent_str(self.total_etfs, self.total))
        print('Фьючерсы:  ', rub_percent_str(self.total_futures, self.total))
        print('Валюта:    ', rub_percent_str(self.total_currencies, self.total))
        print('---------------------------------')
        print('Всего:     ', rub_str(self.total))

    def print_positions(self):
        for figi in self.sums:
            print(
                f'{percent_str(self.sums[figi], self.total)} | {self.names[figi]} | {rub_str(self.sums[figi])} | {figi}')

    def info_dataframe(self) -> pd.DataFrame:
        df_data = [
            ['Aкции', float2f(self.total_shares), percent_str(self.total_shares, self.total)],
            ['Облигации', float2f(self.total_bonds), percent_str(self.total_bonds, self.total)],
            ['Фонды', float2f(self.total_etfs), percent_str(self.total_etfs, self.total)],
            ['Фьючерсы', float2f(self.total_futures), percent_str(self.total_futures, self.total)],
            ['Валюта', float2f(self.total_currencies), percent_str(self.total_currencies, self.total)],
            ['', '', ''],
            ['Всего', float2f(self.total), '']
        ]

        df = pd.DataFrame(df_data)
        df.columns = ['', '', '']
        return df

    def positions_dataframe(self) -> pd.DataFrame:
        df_data = {
            'Имя': [self.names[figi] for figi in self.sums],
            'Сумма': [float2f(self.sums[figi]) for figi in self.sums],
            'Доля': [percent2f(self.sums[figi], self.total) for figi in self.sums]
        }

        return pd.DataFrame(df_data)

    def convert_futures_sum(self, figi: str):
        if Portfolio.contain_prefix(figi, FUTURES_X_1000_FIGIS_PREFIXES):
            self.sums[figi] *= 1000
        if Portfolio.contain_prefix(figi, FUTURES_X_0_01_FIGIS_PREFIXES):
            self.sums[figi] *= 0.01
        if Portfolio.contain_prefix(figi, FUTURES_X_USD_FIGIS_PREFIXES):
            self.sums[figi] *= DOLLAR_CURRENCY


    @staticmethod
    def contain_prefix(figi: str, prefixes: [str]) -> bool:
        for prefix in prefixes:
            if prefix in figi:
                return True
        return False