# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.SoftballBat import SoftballBat


class MrBakey(Enemy):
    def __init__(self):
        super().__init__(
            "Mr.Bakey",
            1,
            2,
            0,
            SoftballBat(),
            "Oh hey Mr.Bakey, how are you doin.",
            Experience()
        )