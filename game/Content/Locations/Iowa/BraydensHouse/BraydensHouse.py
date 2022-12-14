# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.VoiceFromBraydensHead import VoiceFromBraydensHead
from .Enemies.DemonFromUnderBraydensBed import DemonFromUnderBraydensBed
from .Enemies.Chinchilla import Chinchilla
from .Enemies.GuineaPig import GuineaPig
from Content.Characters.BraydenMesserschmidt import BraydenMesserschmidt
from Content.Characters.OliviaMesserschmidt import OliviaMesserschmidt
from Content.Characters.DanMesserschmidt import DanMesserschmidt
from Content.Weapons.BraydensOsuPen import BraydensOsuPen


class BraydensHouse(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Brayden Messerschmidt")
        artifact_families.add("Dan Messerschmidt")
        enemies = ItemList(content_type=Enemy)
        enemies.add(VoiceFromBraydensHead())
        enemies.add(DemonFromUnderBraydensBed())
        enemies.add(Chinchilla())
        enemies.add(GuineaPig())
        enemies.add(BraydenMesserschmidt().create_enemy(BraydensOsuPen()))
        enemies.add(OliviaMesserschmidt().create_enemy())
        enemies.add(DanMesserschmidt().create_enemy())
        super().__init__(
            "Brayden's House",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
