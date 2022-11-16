# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

class RedEvoShield(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Red Evo Shield",
            star_rating,
            "Kelly Krysa",
            Buff(StatTypes.Defense)
        )

class JellyFish(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Jelly Fish",
            star_rating,
            "Kelly Krysa",
            Buff(StatTypes.CritRate)
        )

class Carbine(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Carbine",
            star_rating,
            "Kelly Krysa",
            Buff(StatTypes.Attack)
        )

class Skittles(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Skittles",
            star_rating,
            "Kelly Krysa",
            Buff(StatTypes.Health)
        )

class KunaiKnife(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Kunai Knife",
            star_rating,
            "Kelly Krysa",
            Buff(StatTypes.CritDamage)
        )