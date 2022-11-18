# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class CypireanScythe(Weapon):
    def __init__(self):
        super().__init__(
            "Cypirean Scythe",
            "Long black shaft with 死 imprinted on the blade.",
            "Scythe",
            38,
            Buff(),
            Verbs("swung at", "did a sweeping 360 BayBlade spin at"),
            StarRating(5)
        )
