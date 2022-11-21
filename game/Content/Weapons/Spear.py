# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff


class Spear(Weapon):
    def __init__(self):
        super().__init__(
            "Spear",
            "Just a spear.",
            "Spear",
            6,
            Buff(),
            Verbs("stabbed", "combo'd"),
            StarRating(1)
        )