# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class TrinityForce(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Trinity Force",
            star_rating,
            "Caleb Jalan",
            Buff(StatTypes.Attack, is_percent=True)
        )


class Penjamin(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Penjamin",
            star_rating,
            "Caleb Jalan",
            Buff(StatTypes.CritRate)
        )


class StizzyCart(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Stizzy Cart",
            star_rating,
            "Caleb Jalan",
            Buff(StatTypes.CritDamage, is_percent=True)
        )


class TrinityForce(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Trinity Force",
            star_rating,
            "Caleb Jalan",
            Buff(StatTypes.Attack, is_percent=True)
        )
