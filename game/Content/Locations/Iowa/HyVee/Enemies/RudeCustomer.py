# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Voice import Voice


class RudeCustomer(Enemy):
    def __init__(self):
        super().__init__(
            "A Rude Customer",
            1,
            2,
            0,
            Voice(),
            "The rude customers yelling reminds me of a woman named Karen...",
            Experience()
        )
