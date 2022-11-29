# game packages
# entity packages
from .StatTypes import StatTypes
from .StatValueTypes import StatValueTypes


class StatCollection:
    def __init__(self, stat: StatTypes, value_type: StatValueTypes, amount=0):
        self.stat = stat
        self.value_type = value_type
        self.amount = amount

    def __repr__(self):
        return f"<{self.stat}> {self.amount} [{self.value_type}]"
