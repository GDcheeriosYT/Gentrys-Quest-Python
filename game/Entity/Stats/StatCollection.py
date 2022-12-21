# game packages
# entity packages
from .StatTypes import StatTypes
from .StatValueTypes import StatValueTypes


class StatCollection:
    def __init__(self, stat: StatTypes, value_type: StatValueTypes, is_deductible: bool, amount=0):
        self.stat = stat
        self.value_type = value_type
        self.is_deductible = is_deductible
        self.amount = amount

    def __repr__(self):
        return f"<{self.stat}> {-abs(self.amount) if self.is_deductible else self.amount} [{self.value_type}]"
