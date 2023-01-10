# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Briefcase(Weapon):
    def __init__(self):
        super().__init__(
            "Briefcase",
            "Saul Goodman's briefcase, it has all his work in it so it is pretty heavy.",
            "Club",
            0,
            Buff(),
            Verbs("whammed", "bludgeoned"),
            StarRating(2),
            Experience()
        )