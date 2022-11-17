# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class CapNGoggles(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Cap N' Goggles",
            star_rating,
            "Carter Ballard",
            Buff(StatTypes.CritDamage)
        )

class ModdedXboxController(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Modded Xbox Controller",
            star_rating,
            "Carter Ballard",
            Buff(StatTypes.Attack)
        )

class CartersIphone(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Carter's Iphone",
            star_rating,
            "Carter Ballard",
            Buff(StatTypes.CritRate)
        )

class EpicFBoyNecklace(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Epic F*** Boy Necklace",
            star_rating,
            "Carter Ballard",
            Buff(StatTypes.Health)
        )

class AustinTheElephant(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Austin The Elephant(Stuffed Animal)",
            star_rating,
            "Carter Ballard",
            Buff(StatTypes.Health)
        )


