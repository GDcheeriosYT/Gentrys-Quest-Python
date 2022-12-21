# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class BrodysBroadsword(Weapon):
    def __init__(self):
        super().__init__(
            "Brody's Broadsword",
            "Brody the mighty warrior's broadsword.\nThe weapon was wielded for centuries by Brody himself, but was lost when the great calamity struck and he lost his life to the invading Waifu's.",
            "Broadsword",
            24,
            Buff(StatTypes.Attack),
            Verbs("swung at", "whacked"),
            StarRating(1)
        )
