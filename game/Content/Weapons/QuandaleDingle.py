# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class QuandaleDingle(Weapon):
    def __init__(self):
        super().__init__(
            "Quandale Dingle",
            "Long nose guy",
            "Person",
            46,
            Buff(StatTypes.Attack),
            Verbs("quandale dingle'd", "dingle bombed"),
            StarRating(5)
        )
