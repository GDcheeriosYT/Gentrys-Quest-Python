# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class AnubisBlade(Weapon):
    def __init__(self):
        super().__init__(
            "Anubis Blade",
            "Fried chicken muncher :).",
            "Sword",
            36,
            Buff(StatTypes.Attack),
            Verbs("quandavious bingleton smashed", "placed a goblin giant on the field and it smacked the poop out of"),
            StarRating(4)
        )
