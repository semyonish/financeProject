from bank_stats import BankStats


class Deposit:
    def __init__(self, name:str, value: float, percent: float):
        self.name = name
        self.value = value
        self.percent = percent

        BankStats.addDeposit(self)

    def get_month_income(self) -> float:
        return self.value * self.percent / 100 / 12

    def sum_with_multiplier(self) -> float:
        return self.value

class CreditCard:
    def __init__(self, name:str, value: float):
        self.name = name
        self.value = value

        BankStats.addCredit(self)

    def sum_with_multiplier(self) -> float:
        return self.value * -1
