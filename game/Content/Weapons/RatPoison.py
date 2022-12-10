# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class RatPoison(Weapon):
    def __init__(self):
        super().__init__(
            "Rat Poison",
            "Pete stole some rat poison, dear god what was he going to do with the rat poison. There isn't even any rats here.",
            "Poison",
            35,
            Buff(StatTypes.CritRate),
            Verbs("poured God's fury onto", "demolished all the rat cells of"),
            StarRating(5)
        )