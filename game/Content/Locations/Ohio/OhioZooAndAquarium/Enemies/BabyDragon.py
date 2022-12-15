# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.FireBreath import FireBreath


class BabyDragon(Enemy):
    def __init__(self):
        super().__init__(
            "Baby Dragon",
            3,
            2,
            1,
            FlameBreath(),
            "The Baby Dragon from Clash of Clans is pissed as it is somehow in real life.",
            Experience()
        )
