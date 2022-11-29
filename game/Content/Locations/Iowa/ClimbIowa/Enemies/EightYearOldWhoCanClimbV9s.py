# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.LittleMuscles import LittleMuscles


class EightYearOldWhoClimbV9s(Enemy):
    def __init__(self):
        super().__init__(
            "8 year old who can climb v9s",
            0,
            3,
            0,
            LittleMuscles(),
            "definitely short."
        )
