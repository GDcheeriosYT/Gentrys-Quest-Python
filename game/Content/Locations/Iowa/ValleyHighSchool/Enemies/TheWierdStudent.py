# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.UnchargedChromebook import UnchargedChromebook


class TheWeirdStudent(Enemy):
    def __init__(self):
        super().__init__(
            "The Weird Student",
            1,
            0,
            0,
            UnchargedChromebook(),
            "Oh. Just the weird student.",
            Experience()
        )