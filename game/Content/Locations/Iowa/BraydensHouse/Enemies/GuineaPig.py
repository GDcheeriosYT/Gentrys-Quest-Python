# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Teeth import Teeth


class GuineaPig(Enemy):
    def __init__(self):
        super().__init__(
            "Guinea Pig",
            0,
            1,
            2,
            Teeth(),
            "A Guinea Pig.",
            Experience()
        )
