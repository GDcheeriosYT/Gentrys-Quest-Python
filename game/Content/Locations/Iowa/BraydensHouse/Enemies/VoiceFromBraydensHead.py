# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Psychology import Psychology


class VoiceFromBraydensHead(Enemy):
    def __init__(self):
        super().__init__(
            "Voice From Braydens Head",
            0,
            2,
            1,
            Psychology(),
            "A voice that often talks to Brayden.",
            Experience()
        )
