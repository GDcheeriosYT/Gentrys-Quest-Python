# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Ichimonji(Weapon):
    def __init__(self):
        super().__init__(
            "Ichimonji",
            "A blade wilded by Zoro.\nIs sharp enough to slice the wind.",
            "Katana",
            36,
            Buff(StatTypes.Attack),
            Verbs("sliced", "performed a 100 caliber slice on"),
            StarRating(4)
        )
