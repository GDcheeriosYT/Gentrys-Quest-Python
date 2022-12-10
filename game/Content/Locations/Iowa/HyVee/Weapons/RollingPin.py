# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class RollingPin(Weapon):
    def __init__(self):
        super().__init__(
            "Rolling Pin",
            "Just a regular rolling pin used to club people in the head.",
            "Club",
            0,
            Buff(),
            Verbs("used a rolling pin to hit", "beat"),
            StarRating(2),
            Experience()
        )
