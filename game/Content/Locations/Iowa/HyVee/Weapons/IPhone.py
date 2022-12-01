# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class IPhone(Weapon):
    def __init__(self):
        super().__init__(
            "IPhone",
            "The Karen's IPhone, the letters are huge, her ringer is on, and it has a lot cracks in it.",
            "Club",
            0,
            Buff(),
            Verbs("recorded", "made a rude comment about"),
            StarRating(3),
            Experience()
        )
