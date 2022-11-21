# game packages
# gacha packages
from .Gacha import Gacha

# collection packages
from Collection.Inventory.Inventory import Inventory


class GachaEvent:
    """
    A Gacha Event.
    Used for Stories to obtain weapons and characters

    gacha: Gacha
        the gacha to pull from

    is_weapon: bool
        weather or not you'll pull a weapon

    amount: int
        the amount you'll pull from the gacha

    """

    gacha = None
    is_weapon = None
    amount = None

    def __init__(self, gacha: Gacha, is_weapon: bool, amount: int):
        self.gacha = gacha
        self.is_weapon = is_weapon
        self.amount = amount

    def pull(self, inventory: Inventory):
        pulls = []
        for i in range(self.amount):
            if self.is_weapon:
                pulls.append(self.gacha.pull_weapon())

            else:
                pulls.append(self.gacha.pull_character())

        self.gacha.generate_output(pulls, inventory)