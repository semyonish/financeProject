DEPOSITS = []
CREDITS = []

class Deposit:
    def __init__(self, value: float, percent: float):
        self.value = value
        self.percent = percent

        global DEPOSITS
        DEPOSITS += [self]

    def get_month_income(self) -> float:
        return self.value * self.percent / 100 / 12

    def sum_with_multiplier(self) -> float:
        return self.value

class CreditCard:
    def __init__(self, value: float):
        self.value = value

        global CREDITS
        CREDITS += [self]

    def sum_with_multiplier(self) -> float:
        return self.value * -1