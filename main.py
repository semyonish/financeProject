from datetime import datetime

import pandas as pd

from t_client import TMergeClient
from bank_stats import BankStats
from stats import Portfolio
from values import TOKENS

if __name__ == '__main__':
    print(datetime.now().date())
    print('=======================================================================')

    client = TMergeClient(TOKENS)

    portfolio = Portfolio(client.portfolios)
    portfolio.print_info()
    print('=======================================================================')
    print(portfolio.positions_dataframe())
    print('=======================================================================')
    print(BankStats.info_dataframe())

    with pd.ExcelWriter(f'data/{datetime.now().date()}.xlsx') as writer:
        portfolio.info_dataframe().to_excel(writer, sheet_name='Info', index=False, header=False)
        portfolio.positions_dataframe().to_excel(writer, sheet_name='Positions', index=False)
        BankStats.info_dataframe().to_excel(writer, sheet_name='Bank', index=False, header=False)
