# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Zebra(Weapon):
    def __init__(self):
        super().__init__(
            "Zebra",
            "Just a scanner phone."
            "Phone",
            0,
            Buff(),
            Verbs("scanned", ""),
            StarRating(5),
            Experience()
        )
