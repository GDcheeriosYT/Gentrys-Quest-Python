# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Hands(Weapon):
    def __init__(self):
        super().__init__(
            "Hands",
            "These are nice and beat up. Wait why are you using someone else's hands?",
            "Hands",
            0,
            Buff(),
            Verbs("punched", "beat"),
            StarRating(1),
            Experience()
        )
