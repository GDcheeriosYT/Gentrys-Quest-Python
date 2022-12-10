# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.MeatCleaver import MeatCleaver


class Butcher(Enemy):
    def __init__(self):
        super().__init__(
            "Butcher",
            2,
            3,
            1,
            MeatCleaver(),
            "He is a master of the cleaver, unfortunately he is trying to kill you.",
            Experience()
        )
