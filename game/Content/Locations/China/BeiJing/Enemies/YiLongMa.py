# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Money import Money


class YiLongMa(Enemy):
    def __init__(self):
        super().__init__(
            "Yi Long Ma",
            5,
            4,
            4,
            Money(),
            "Elon Musk's half brother from China.",
            Experience()
        )
