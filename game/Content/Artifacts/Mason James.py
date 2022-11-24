# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

class UsedUndies(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Used Undies",
            star_rating,
            "Mason James",
            Buff(StatTypes.Health)
        )

class HairBrush(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "HairBrush",
            star_rating,
            "Mason James",
            Buff(StatTypes.Attack)
        )

class HandCuffs(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Hand Cuffs",
            star_rating,
            "Mason James",
            Buff(StatTypes.Defense)
        )

class Restraints(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Restraints",
            star_rating,
            "Mason James",
            Buff(StatTypes.CritRate)
        )

class StrangeFlashlight(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "StrangeFlashlight",
            star_rating,
            "Mason James",
            Buff(StatTypes.CritDamage)
        )