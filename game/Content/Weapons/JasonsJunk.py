# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class JasonsJunk(Weapon):
    def __init__(self):
        super().__init__(
            "Jason's Junk",
            "It's Jason's. From Hy-vee. Estimated 14 inches.",
            "Penis",
            42,
            Buff(StatTypes.Health),
            Verbs("wanked", "cumblasted"),
            StarRating(5)
        )
