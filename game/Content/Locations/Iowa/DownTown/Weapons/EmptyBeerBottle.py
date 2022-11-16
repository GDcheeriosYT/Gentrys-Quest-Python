# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class EmptyBeerBottle(Weapon):
    def __init__(self):
        super().__init__(
            "Empty Beer Bottle",
            "A beer bottle in a brown paper bag.",
            "Bottle",
            0,
            Buff(),
            Verbs("whacked", "peed on"),
            StarRating(1),
            Experience()
        )
