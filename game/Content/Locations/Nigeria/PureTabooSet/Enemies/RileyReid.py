# game packages
# entity pacakges
from Entity.Enemy.Enemy import Enemy

# content packages
from ..Weapons.HandOfExhaust import HandOfExhaust


class RileyReid(Enemy):
    def __init__(self):
        super().__init__(
            "Riley Reid",
            5,
            3,
            1,
            HandOfExhaust(),
            "Popular Actress"
        )