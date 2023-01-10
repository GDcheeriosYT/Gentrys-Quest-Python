# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class LiverBoostedHands(Weapon):
    def __init__(self):
        super().__init__(
            "Liver Boosted Hands",
            "The liver and gear boosted hands are much stronger pairs of the regular hands.",
            "Hands",
            4,
            Buff(),
            Verbs("beat", "beat up"),
            StarRating(5),
            Experience()
        )