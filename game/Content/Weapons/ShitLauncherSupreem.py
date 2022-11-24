# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class ShitLauncherSupreem(Weapon):
    def __init__(self):
        super().__init__(
            "Shit Launcher Supreem",
            "The sequel to the noob tube.",
            "Grenade Launcher",
            41,
            Buff(StatTypes.Defense),
            Verbs("glooped on", "sharted on"),
            StarRating(5)
        )
