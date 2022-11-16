# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class KeyCard(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Key Card",
            star_rating,
            "Max Shrum",
            Buff(StatTypes.CritRate)
        )

class BowlOfNoodles(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Bowl of Noodles",
            star_rating,
            "Max Shrum",
            Buff(StatTypes.Health)
        )

class BikeTirePump(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Bike Tire Pump",
            star_rating,
            "Max Shrum",
            Buff(StatTypes.Attack)
        )

class Blueprints(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Blueprints",
            star_rating,
            "Max Shrum",
            Buff(StatTypes.Defense)
        )

class Violin(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Violin",
            star_rating,
            "Max Shrum",
            Buff(StatTypes.Health)
        )
