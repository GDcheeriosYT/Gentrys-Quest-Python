# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.OshaWorker import OshaWorker


class UnfinishedConstructionSite(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Max Shrum")
        enemies = ItemList(content_type=Enemy)
        enemies.add(OshaWorker())
        super().__init__(
            "Unfinished Construction Site",
            1,
            artifact_families,
            enemies,
            True,
            True
        )
