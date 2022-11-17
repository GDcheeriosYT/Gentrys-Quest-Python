# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.FeralLunchLady import FeralLunchLady
from .Enemies.FlyingPencil import FlyingPencil
from .Enemies.MrBakey import MrBakey
from .Enemies.RacoonInsideABackpack import RacoonInsideABackpack
from .Enemies.TheWierdStudent import TheWeirdStudent
from .Enemies.TheLocalSecurityGuard import TheLocalSecurityGuard

class ValleyHighSchool(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Brayden Messerschmidt")
        artifact_families.add("Carter Ballard")
        artifact_families.add("Lucas Smidt")
        artifact_families.add("Nathan Tenney")
        enemies = ItemList(content_type=Enemy)
        enemies.add(FeralLunchLady())
        enemies.add(FlyingPencil())
        enemies.add(MrBakey())
        enemies.add(RacoonInsideABackpack())
        enemies.add(TheWeirdStudent())
        enemies.add(TheLocalSecurityGuard())
        super().__init__(
            "Valley High School",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
