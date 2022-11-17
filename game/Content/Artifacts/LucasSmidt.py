# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Computer(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Computer",
            star_rating,
            "Lucas Smidt",
            Buff(StatTypes.CritRate)
        )


class ProteinShake(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Protein Shake",
            star_rating,
            "Lucas Smidt",
            Buff(StatTypes.Health)
        )


class Basketball(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Basketball",
            star_rating,
            "Lucas Smidt",
            Buff(StatTypes.Attack)
        )


class Piano(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Piano",
            star_rating,
            "Lucas Smidt",
            Buff(StatTypes.CritDamage)
        )


class TardySlip(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "TardySlip",
            star_rating,
            "Lucas Smidt",
            Buff(StatTypes.Attack)
        )
