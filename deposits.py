class Deposit:
    def __init__(self, name: str, value: float, percent: float):
        self.name = name
        self.value = value
        self.percent = percent

    def get_month_income(self) -> float:
        return self.value * self.percent / 100 / 12


class CreditCard:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value
