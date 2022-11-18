# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class NutBuster(Weapon):
    def __init__(self):
        super().__init__(
            "Nut buster",
            "Perfect weapon to slide on your opps and bust their nuts.",
            "Mace",
            25,
            Buff(StatTypes.Attack),
            Verbs("busted", "busted the nuts of"),
            StarRating(4)
        )
