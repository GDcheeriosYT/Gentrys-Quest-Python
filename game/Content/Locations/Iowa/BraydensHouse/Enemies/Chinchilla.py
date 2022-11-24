# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Paws import Paws


class Chinchilla(Enemy):
    def __init__(self):
        super().__init__(
            "Chinchilla",
            0,
            1,
            1,
            Paws(),
            "Just a normal pet chinchilla.",
            Experience()
        )
