# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.PaperKnife import PaperKnife


class SentientPileOfHomework(Enemy):
    def __init__(self):
        super().__init__(
            "Sentient Pile Of Homework",
            0,
            1,
            1,
            PaperKnife(),
            "Not Again! My homework is trying to kill me!",
            Experience()
        )
