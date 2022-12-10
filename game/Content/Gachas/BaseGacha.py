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

# characters
from Content.Characters.KellyKrysa import KellyKrysa
from Content.Characters.DanMesserschmidt import DanMesserschmidt
from Content.Characters.MasonBorland import MasonBorland
from Content.Characters.OliviaMesserschmidt import OliviaMesserschmidt
from Content.Characters.KchuntMan import KchuntMan
from Content.Characters.JayceeMaiers import JayceeMaiers
from Content.Characters.JackBorland import JackBorland
from Content.Characters.JackSmidt import JackSmidt
from Content.Characters.HentaiMan import HentaiMan
from Content.Characters.MakDaddy import MakDaddy
from Content.Characters.MatheuSliger import MatheuSliger
from Content.Characters.Shrpe import Shrpe


class BaseGacha(Gacha):
    def __init__(self):
        super().__init__(
            Text("Base Game"),
            [
                KellyKrysa(),
                DanMesserschmidt(),
                MasonBorland(),
                OliviaMesserschmidt(),
                KchuntMan(),
                JayceeMaiers(),
                JackBorland(),
                JackSmidt(),
                HentaiMan(),
                MakDaddy(),
                MatheuSliger(),
                Shrpe()
            ],
            [
                Sword(),
                Bow(),
                Spear(),
                Hammer()
            ],
            100
        )
