# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.LunchTrayWithFoodOnIt import LunchTrayWithFoodOnIt


class FeralLunchLady(Enemy):
    def __init__(self):
        super().__init__(
            "Feral Lunch Lady",
            1,
            2,
            2,
            LunchTrayWithFoodOnIt(),
            "AHHHHH! The lunch lady has gone Feral!",
            Experience()
        )