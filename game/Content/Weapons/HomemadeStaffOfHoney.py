# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class HomemadeStaffOfHoney(Weapon):
    def __init__(self):
        super().__init__(
            "Homemade Staff of Honey",
            "A pointy staff of honey.",
            "Staff",
            20,
            Buff(StatTypes.CritRate),
            Verbs("stabbed", "enlightened"),
            StarRating(3)
        )
