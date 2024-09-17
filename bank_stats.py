import pandas as pd

from deposits import Deposit, CreditCard


class BankStats:
    DEPOSITS: [Deposit] = []
    CREDITS: [CreditCard] = []

    def addDeposit(dep: Deposit):
        BankStats.DEPOSITS += [dep]

    def addCredit(credit: CreditCard):
        BankStats.CREDITS += [credit]

    @staticmethod
    def info_dataframe() -> pd.DataFrame:
        df_data = []

        df = pd.DataFrame(df_data)
        return df