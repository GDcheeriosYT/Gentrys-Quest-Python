# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Teeth(Weapon):
    def __init__(self):
        super().__init__(
            "Teeth",
            "Teeth on a guinea pig.",
            "Teeth",
            0,
            Buff(),
            Verbs("bit", "chomped on"),
            StarRating(2),
            Experience()
        )