from enum import Enum


class DepositAvailability(Enum):
    FAST = 1
    USUAL = 2
    SLOW = 3

class Deposit:
    def __init__(self, name: str, value: float, percent: float, availability: DepositAvailability = DepositAvailability.USUAL):
        self.name = name
        self.value = value
        self.percent = percent
        self.availability = availability

    def get_month_income(self) -> float:
        return self.value * self.percent / 100 / 12

    def get_available_value(self, availability: DepositAvailability):
        return self.value if self.availability.value <= availability.value else 0


class CreditCard:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value
