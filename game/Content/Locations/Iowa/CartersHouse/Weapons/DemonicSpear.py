# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class DemonicSpear(Weapon):
    def __init__(self):
        super().__init__(
            "Demonic Spear",
            "Demonic Spear used by the guard who guards Carter's Bedroom.",
            "Spear",
            10,
            Buff(),
            Verbs("stabbed", "pierced"),
            StarRating(2),
            Experience()
        )
