import pandas as pd

from deposits import Deposit, CreditCard
from useful_functions import float2f


class BankStats:
    DEPOSITS: [Deposit] = []
    CREDITS: [CreditCard] = []

    def add_deposit(dep: Deposit):
        BankStats.DEPOSITS += [dep]

    def add_credit(credit: CreditCard):
        BankStats.CREDITS += [credit]

    @staticmethod
    def info_dataframe() -> pd.DataFrame:
        month_income_sum = 0
        deposit_sum = 0
        credit_sum = 0

        df_data = [['Депозиты', '', '', '']]
        df_data += [['Имя', 'Сумма', 'Проценты', 'Месячный доход']]

        for deposit in BankStats.DEPOSITS:
            month_income = deposit.get_month_income()
            month_income_sum += month_income
            deposit_sum += deposit.value
            df_data += [[deposit.name, float2f(deposit.value), float2f(deposit.percent), float2f(month_income)]]

        df_data += [['', '', '', '']]
        df_data += [['Всего', float2f(deposit_sum), '', float2f(month_income_sum)]]
        df_data += [['', '', '', '']]
        df_data += [['Кредиты', '', '', '']]
        df_data += [['Имя', 'Сумма', '', '']]

        for credit in BankStats.CREDITS:
            df_data += [[credit.name, float2f(credit.value), '', '']]
            credit_sum += credit.value

        df_data += [['', '', '', '']]
        df_data += [['Всего', float2f(credit_sum), '', '']]

        df_data += [['', '', '', '']]
        df_data += [['Баланс', float2f(deposit_sum - credit_sum), '', '']]

        df = pd.DataFrame(df_data)
        return df