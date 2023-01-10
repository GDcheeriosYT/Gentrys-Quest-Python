# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.TeslaStock import TeslaStock


class ElonMusk(Enemy):
    def __init__(self):
        super().__init__(
            "Elon Musk",
            4,
            3,
            3,
            TeslaStock(),
            "Elon Musk (brother of Yi Long Ma) owns many companies, he is also an absolute UNIT.",
            Experience()
        )
