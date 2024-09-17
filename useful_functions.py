import pandas as pd
from tinkoff.invest import MoneyValue, Quotation, Account, PortfolioResponse, PortfolioPosition

from instruments import Instruments


def money_value_str(val: MoneyValue) -> str:
    return str(val.units + val.nano * 10 ** -9) + ' ' + val.currency


def money_value_float(val: MoneyValue) -> float:
    return val.units + val.nano * 10 ** -9


def quotation_str(val: Quotation) -> str:
    return str(val.units + val.nano * 10 ** -9)


def quotation_float(val: Quotation) -> float:
    return val.units + val.nano * 10 ** -9


def accounts_dataframe(accounts: [Account]) -> pd.DataFrame:
    df_list = []

    for account in accounts:
        df_list += [
            [account.id,
             account.name,
             str(account.status).split('_')[-1],
             str(account.type).split('_')[-1]]]

    df = pd.DataFrame(df_list)
    df.index = [''] * len(accounts)
    df.columns = ['id', 'name', 'status', 'type']
    return df


def show_portfolio_stats(portfolio: PortfolioResponse):
    shares = portfolio.total_amount_shares
    bonds = portfolio.total_amount_bonds
    etfs = portfolio.total_amount_etf
    futures = portfolio.total_amount_futures
    currencies = portfolio.total_amount_currencies
    exp_yield = portfolio.expected_yield
    total = portfolio.total_amount_portfolio

    print('---------------------------------')
    print('Акции: ', money_value_str(shares))
    print('Облигации: ', money_value_str(bonds))
    print('Фонды: ', money_value_str(etfs))
    print('Фьючерсы: ', money_value_str(futures))
    print('Валюта: ', money_value_str(currencies))
    print('---------------------------------')
    print('Всего: ', money_value_str(total))
    print('Прибыль: ', quotation_str(exp_yield) + '%')
    print('---------------------------------')


def positions_df(positions: [PortfolioPosition]) -> pd.DataFrame:
    positions_df_list = []
    for position in positions:
        instrument = Instruments.get(position.figi)
        positions_df_list += [[
            instrument.figi,
            instrument.name,
            instrument.instrument_type,
            instrument.country_of_risk_name,
            money_value_str(position.current_price),
            quotation_str(position.quantity),
            quotation_str(position.expected_yield) + ' ' + instrument.currency,
            money_value_str(position.average_position_price),
            money_value_str(position.average_position_price_fifo),
            quotation_str(position.average_position_price_pt),
            money_value_str(position.current_nkd)
        ]]

    positions_df = pd.DataFrame(positions_df_list)
    positions_df.index = [''] * len(positions)
    positions_df.columns = [
        'figi',
        'name',
        'type',
        'country',
        'price',
        'quantity',
        'yield',
        'average_price',
        'average_price_FIFO',
        'average_price_pt',
        'nkd'
    ]
    return positions_df

def float2f(value: float) -> str:
    return f'{value:.2f}'

def percent2f(value: float, total: float) -> str:
    return f'{100 * value / total:.2f}'

def percent_str(value: float, total: float) -> str:
    return f'{percent2f(value, total)}%'

def rub_str(value: float) -> str:
    return f'{value:.2f} rub'

def rub_percent_str(value: float, total: float) -> str:
    return f'{rub_str(value)} ({percent_str(value, total)})'
