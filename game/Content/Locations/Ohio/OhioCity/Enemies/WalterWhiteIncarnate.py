# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.BlueMeth import BlueMeth


class WalterWhiteIncarnate(Enemy):
    def __init__(self):
        super().__init__(
            "Walter White Incarnate",
            2,
            2,
            2,
            BlueMeth(),
            "Walter White has come back from the dead to cook more blue meth.",
            Experience()
        )
