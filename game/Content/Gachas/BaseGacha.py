# game packages
# gacha packages
from Gacha.Gacha import Gacha

# graphics packages
from Graphics.Text.Text import Text

# content packages
# weapons
from Content.Weapons.Sword import Sword
from Content.Weapons.Bow import Bow
from Content.Weapons.Spear import Spear
from Content.Weapons.Hammer import Hammer


class BaseGacha(Gacha):
    def __init__(self):
        super().__init__(
            Text("Base Game"),
            [],
            [
                Sword(),
                Bow(),
                Spear(),
                Hammer()
            ],
            100
        )
