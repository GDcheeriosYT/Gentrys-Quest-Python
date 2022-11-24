# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff


class Sword(Weapon):
    def __init__(self):
        super().__init__(
            "Sword",
            "Just a sword.",
            "Sword",
            5,
            Buff(),
            Verbs("swung at", "sliced up"),
            StarRating(1)
        )