# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class SoftballBat(Weapon):
    def __init__(self):
        super().__init__(
            "Softball Bat",
            "Mr.Bakey teaches softball that is why he has a softball bat.",
            "club",
            0,
            Buff(),
            Verbs("bonked", "bludgeoned"),
            StarRating(2),
            Experience()
        )
