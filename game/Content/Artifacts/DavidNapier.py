# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class DavidsGoldenAmuletOfMotherlessness(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Davids Golden Amulet of Motherlessnesss",
            star_rating,
            "David Napier",
            Buff(StatTypes.Health)
        )


class TitaniumStiltsForShortKings(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Titanium Stilts For Short Kings",
            star_rating,
            "David Napier",
            Buff(StatTypes.Defense)
        )


class HeadBangersGuitarOfLoneliness(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Head Banger's Guitar of Loneliness",
            star_rating,
            "David Napier",
            Buff(StatTypes.CritDamage)
        )


class FidgetSpinner(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Fidget Spinner",
            star_rating,
            "David Napier",
            Buff(StatTypes.Attack)
        )


class PictureOfChildScreaming(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Picture of Child Screaming",
            star_rating,
            "David Napier",
            Buff()
        )
