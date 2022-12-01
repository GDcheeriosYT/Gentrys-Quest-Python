# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Voice(Weapon):
    def __init__(self):
        super().__init__(
            "Voice",
            "How do you use your voice as weapon?",
            "Voice",
            0,
            Buff(),
            Verbs("scolded", "yelled at"),
            StarRating(2),
            Experience()
        )
