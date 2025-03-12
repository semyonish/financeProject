import pandas as pd

from deposits import Deposit, CreditCard, DepositAvailability
from useful_functions import float2f


class BankStats:
    DEPOSITS: [Deposit] = []
    CREDITS: [CreditCard] = []

    @staticmethod
    def add_deposit(dep: Deposit):
        BankStats.DEPOSITS += [dep]

    @staticmethod
    def add_credit(credit: CreditCard):
        BankStats.CREDITS += [credit]

    @staticmethod
    def deposit_sum(availability: DepositAvailability) -> float:
        return sum(map(lambda dep: dep.get_available_value(availability), BankStats.DEPOSITS))

    @staticmethod
    def deposit_month_income() -> float:
        return sum(map(lambda dep: dep.get_month_income(), BankStats.DEPOSITS))

    @staticmethod
    def credit_sum() -> float:
        return sum(map(lambda credit: credit.value, BankStats.CREDITS))

    @staticmethod
    def balance(availability: DepositAvailability = DepositAvailability.USUAL) -> float:
        return BankStats.deposit_sum(availability) - BankStats.credit_sum()

    @staticmethod
    def info_dataframe() -> pd.DataFrame:
        df_data = [['Депозиты', '', '', '']]
        df_data += [['Имя', 'Сумма', 'Проценты', 'Месячный доход']]

        for deposit in BankStats.DEPOSITS:
            df_data += [
                [deposit.name, float2f(deposit.value), float2f(deposit.percent), float2f(deposit.get_month_income())]]

        df_data += [['', '', '', '']]
        df_data += [['Всего', float2f(BankStats.deposit_sum(DepositAvailability.USUAL)), '', float2f(BankStats.deposit_month_income())]]
        df_data += [['', '', '', '']]
        df_data += [['Кредиты', '', '', '']]
        df_data += [['Имя', 'Сумма', '', '']]

        for credit in BankStats.CREDITS:
            df_data += [[credit.name, float2f(credit.value), '', '']]

        df_data += [['', '', '', '']]
        df_data += [['Всего', float2f(BankStats.credit_sum()), '', '']]

        df_data += [['', '', '', '']]
        df_data += [['Баланс быстро', float2f(BankStats.balance(DepositAvailability.FAST)), '', '']]
        df_data += [['Баланс средне', float2f(BankStats.balance()), '', '']]
        df_data += [['Баланс', float2f(BankStats.balance(DepositAvailability.SLOW)), '', '']]

        df = pd.DataFrame(df_data)
        return df
