# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class ChopSticks(Weapon):
    def __init__(self):
        super().__init__(
            "Chopsticks",
            "Just chopsticks.",
            "Chopsticks",
            50,
            Buff(),
            Verbs("jabbed", "poked the eyes of"),
            StarRating(5)
        )
