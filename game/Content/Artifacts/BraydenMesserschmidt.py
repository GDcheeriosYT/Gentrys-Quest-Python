# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class MadokaChibiPlush(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Madoka Chibi Plush",
            star_rating,
            "Brayden Messerschmidt",
            Buff(StatTypes.CritRate)
        )


class LoliCloth(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Loli Cloth",
            star_rating,
            "Brayden Messerschmidt",
            Buff(StatTypes.CritRate)
        )


class LoliBodyPillow(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Loli Body Pillow",
            star_rating,
            "Brayden Messerschmidt",
            Buff(StatTypes.CritRate)
        )


class PepsiBottle(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Pepsi Bottle",
            star_rating,
            "Brayden Messerschmidt",
            Buff(StatTypes.CritRate)
        )


class OsuTablet(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Osu Tablet",
            star_rating,
            "Brayden Messerschmidt",
            Buff(StatTypes.CritRate)
        )