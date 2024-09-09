import pandas as pd
from tinkoff.invest import MoneyValue, Quotation, Account, PortfolioResponse, PortfolioPosition


def money_value_str(val: MoneyValue) -> str:
    return str(val.units + val.nano * 10**-9) + ' ' + val.currency

def money_value_int(val: MoneyValue) -> int:
    return val.units + val.nano * 10**-9

def quotation_str(val: Quotation) -> str:
    return str(val.units + val.nano * 10**-9)

def quotation_int(val: Quotation) -> int:
    return val.units + val.nano * 10**-9

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

    print('Акции: ', money_value_str(shares))
    print('Облигации: ', money_value_str(bonds))
    print('Фонды: ', money_value_str(etfs))
    print('Фьючерсы: ', money_value_str(futures))
    print('Валюта: ', money_value_str(currencies))
    print('---------------------------------')
    print('Прибыль: ', quotation_str(exp_yield) + '%')