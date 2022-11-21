# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff


class Bow(Weapon):
    def __init__(self):
        super().__init__(
            "Bow",
            "Just a bow.",
            "Bow",
            3,
            Buff(),
            Verbs("shot", "hit the bullseye of"),
            StarRating(1)
        )