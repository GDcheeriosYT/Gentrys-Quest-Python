# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class TeslaCanon(Weapon):
    def __init__(self):
        super().__init__(
            "Tesla Canon",
            "Winton Gun:).",
            "Tesla",
            0,
            Buff(),
            Verbs("zapped", "shocked"),
            StarRating(5),
            Experience()
        )