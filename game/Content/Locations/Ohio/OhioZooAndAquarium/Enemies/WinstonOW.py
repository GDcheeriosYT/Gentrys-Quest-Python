# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.TeslaCanon import TeslaCanon


class WinstonOW(Enemy):
    def __init__(self):
        super().__init__(
            "Winton Overwat",
            5,
            1,
            2,
            TeslaCanon(),
            "Winton Overwat...........",
            Experience()
        )
