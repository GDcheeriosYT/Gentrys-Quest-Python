# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Zebra import Zebra


class TargetManager(Enemy):
    def __init__(self):
        weapon = Zebra()
        weapon.verbs.critical = "dealt with"
        super().__init__(
            "Target Manager",
            1,
            2,
            2,
            weapon,
            "A manager",
            Experience()
        )
