# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class BraydensOsuPen(Weapon):
    def __init__(self):
        super().__init__(
            "Brayden's osu pen",
            "Brayden's osu pen.",
            "Pen",
            46,
            Buff(StatTypes.CritRate),
            Verbs("hit a circle on", "fc'ed the pattern on"),
            StarRating(5)
        )
