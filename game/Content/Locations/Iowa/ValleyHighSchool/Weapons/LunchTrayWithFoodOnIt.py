# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class LunchTrayWithFoodOnIt(Weapon):
    def __init__(self):
        super().__init__(
            "Lunch Tray with Lunch on It",
            "It is a lunch tray with food on it.",
            "sword",
            1,
            Buff(),
            Verbs("slapped", "grossed out"),
            StarRating(3),
            Experience()
        )
