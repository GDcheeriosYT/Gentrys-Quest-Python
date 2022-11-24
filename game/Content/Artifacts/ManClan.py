# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class Phone(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Phone",
            star_rating,
            "Man Clan",
            Buff(StatTypes.CritDamage)
        )


class SpoonCollection(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Spoon Collection",
            star_rating,
            "Man Clan",
            Buff(StatTypes.Health)
        )


class CrustyBodyPillow(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Crusty Body Pillow",
            star_rating,
            "Man Clan",
            Buff(StatTypes.Defense)
        )


class BluetoothSpeakerThatPlaysVineBoomSoundEffect(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Bluetooth Speaker That Plays Vine Boom Sound Effect",
            star_rating,
            "Man Clan",
            Buff(StatTypes.Health)
        )


class SoakedDoujin(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Soaked Doujin",
            star_rating,
            "Man Clan",
            Buff(StatTypes.CritRate)
        )
