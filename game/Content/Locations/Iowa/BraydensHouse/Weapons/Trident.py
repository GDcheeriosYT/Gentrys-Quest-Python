# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Trident(Weapon):
    def __init__(self):
        super().__init__(
            "Trident",
            "A demon's trident.",
            "Trident",
            0,
            Buff(),
            Verbs("poked", "impaled"),
            StarRating(2),
            Experience()
        )
