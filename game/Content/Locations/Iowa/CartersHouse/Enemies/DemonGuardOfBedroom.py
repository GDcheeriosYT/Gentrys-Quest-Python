# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.DemonicSpear import DemonicSpear


class DemonGuardOfBedroom(Enemy):
    def __init__(self):
        super().__init__(
            "Demon Guarding Carter's room",
            0,
            1,
            2,
            DemonicSpear(),
            "He is guarding something sacred.",
            Experience()
        )
