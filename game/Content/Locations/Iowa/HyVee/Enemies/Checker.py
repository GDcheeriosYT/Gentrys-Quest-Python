# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Scanner import Scanner


class Checker(Enemy):
    def __init__(self):
        super().__init__(
            "Checker",
            2,
            1,
            0,
            Scanner(),
            "Good ol' HyVee checkout guy... or girl I guess.",
            Experience()
        )
