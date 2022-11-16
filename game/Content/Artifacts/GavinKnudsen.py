# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

class NutCracker(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Nut Cracker",
            star_rating,
            "Gavin Knudsen",
            Buff(StatTypes.Defense)
        )

class SaltyNuts(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Salty Nuts",
            star_rating,
            "Gavin Knudsen",
            Buff(StatTypes.Health)
        )

class BowlOfNuts(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Bowl Of Nuts",
            star_rating,
            "Gavin Knudsen",
            Buff(StatTypes.CritDamage)
        )

class SecretSauce(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Secret Sauce",
            star_rating,
            "Gavin Knudsen",
            Buff(StatTypes.Health)
        )

class EmptyPringlesCan(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Empty Pringles Can",
            star_rating,
            "Gavin Knudsen",
            Buff(StatTypes.Attack)
        )