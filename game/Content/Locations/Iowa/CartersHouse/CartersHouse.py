# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.HarryTheDog import HarryTheDog
from .Enemies.AngryParents import AngryParents
from .Enemies.SentientPileOfHomework import SentientPileOfHomework
from .Enemies.DemonGuardOfBedroom import DemonGuardOfBedroom
from .Enemies.TheRacoon import TheRacoon

class CartersHouse(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Carter Ballard")
        enemies = ItemList(content_type=Enemy)
        enemies.add(HarryTheDog())
        enemies.add(AngryParents())
        enemies.add(SentientPileOfHomework())
        enemies.add(DemonGuardOfBedroom())
        enemies.add(TheRacoon())
        super().__init__(
            "Carter's House",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
