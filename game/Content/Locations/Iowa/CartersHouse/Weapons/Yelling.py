# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Yelling(Weapon):
    def __init__(self):
        super().__init__(
            "Yelling",
            "The power to yell as hard as your angry parents.",
            "Voice",
            20,
            Buff(),
            Verbs("screamed at", "yelled at"),
            StarRating(3),
            Experience()
        )
