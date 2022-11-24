# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class VialOfPiss(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Vial of Piss",
            star_rating,
            "Grant Wiseman",
            Buff()
        )
