# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Pan import Pan


class ChineseChef(Enemy):
    def __init__(self):
        super().__init__(
            "Chinese Chef",
            2,
            2,
            0,
            Pan(),
            "He does make some mean General Chicken.",
            Experience()
        )
