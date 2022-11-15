# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Trident import Trident


class DemonFromUnderBraydensBed(Enemy):
    def __init__(self):
        super().__init__(
            "Demons From Under Brayden's Bed",
            1,
            1,
            0,
            Trident(),
            "A demon from underneath brayden's bed.",
            Experience()
        )
