# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class SharpPencil(Weapon):
    def __init__(self):
        super().__init__(
            "Sharp Pencil",
            "It was apart of Flying Pencil's body.",
            "Spear",
            0,
            Buff(),
            Verbs("stabbed", "poked"),
            StarRating(2),
            Experience()
        )
