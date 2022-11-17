# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class BlackDildo(Artifact):
    def init(self, star_rating):
        super().__init__(
            "Black Dildo",
            star_rating,
            "Lethal Weapon",
            Buff(StatTypes.CritDamage)
        )