# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.BusinessMan import BusinessMan
from .Enemies.HomelessGuy import HomelessGuy


class DownTown(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Down Town")
        enemies = ItemList(content_type=Enemy)
        enemies.add(BusinessMan())
        enemies.add(HomelessGuy())
        super().__init__(
            "Down Town",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
