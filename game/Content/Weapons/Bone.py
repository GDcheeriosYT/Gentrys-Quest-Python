# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Bone(Weapon):
    def __init__(self):
        super().__init__(
            "Bone",
            "4 foot long dog bone",
            "Sword",
            26,
            Buff(),
            Verbs("clobbered", "smushed"),
            StarRating(2)
        )
