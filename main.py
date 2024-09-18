from datetime import datetime

import pandas as pd

from TClient import TMergeClient
from bank_stats import BankStats
from stats import Portfolio
from values import TOKENS

if __name__ == '__main__':
    print(datetime.now().date())

    client = TMergeClient(TOKENS)

    portfolio = Portfolio(client.portfolios)
    portfolio.print_info()
    portfolio.print_positions()
    print(BankStats.info_dataframe())

    with pd.ExcelWriter(f'data/{datetime.now().date()}.xlsx') as writer:
        portfolio.info_dataframe().to_excel(writer, sheet_name='Info', index=False, header=False)
        portfolio.positions_dataframe().to_excel(writer, sheet_name='Positions', index=False)
        BankStats.info_dataframe().to_excel(writer, sheet_name='Банк', index=False, header=False)

    # print(sum(map(lambda x: x.get_month_income(), DEPOSITS)))
    # print(sum(map(lambda x: x.sum_with_multiplier(), ALL_BANK)))
