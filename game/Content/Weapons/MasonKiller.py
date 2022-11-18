# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class MasonKiller(Weapon):
    def __init__(self):
        super().__init__(
            "Mason Killer",
            "Two purple daggers",
            "Dagger",
            50,
            Buff(StatTypes.Attack),
            Verbs("penetrated", "hard penetrated"),
            StarRating(5)
        )
