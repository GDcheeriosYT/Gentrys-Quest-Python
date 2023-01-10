# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class FinsAndFlippers(Weapon):
    def __init__(self):
        super().__init__(
            "Fins and Flippers",
            "These are fins and flippers. They have the name *Bryan* on them...",
            "Fins",
            0,
            Buff(),
            Verbs("slaps", "splashes"),
            StarRating(1),
            Experience()
        )