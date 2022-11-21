# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class KnutsHamemr(Weapon):
    def __init__(self):
        super().__init__(
            "Knuts Hammer",
            "The Massive Knuts Hammer.\nWas picked up by the first great lord knuts and used to slay all the oppositions. lol ##",
            "Hammer",
            50,
            Buff(StatTypes.Defense),
            Verbs("knut slammed", "atomically slammed"),
            StarRating(5)
        )
