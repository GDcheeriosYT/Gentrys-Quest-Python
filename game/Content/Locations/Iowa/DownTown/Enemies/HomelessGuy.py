# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.EmptyBeerBottle import EmptyBeerBottle


class HomelessGuy(Enemy):
    def __init__(self):
        super().__init__(
            "Homeless Guy",
            0,
            0,
            0,
            EmptyBeerBottle(),
            "A Homeless Guy.",
            Experience()
        )
