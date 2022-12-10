# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Muscles import Muscles


class GymBro(Enemy):
    def __init__(self):
        super().__init__(
            "Gym Bro",
            1,
            1,
            1,
            Muscles(),
            "probably short."
        )
