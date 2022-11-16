# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.TargetEmployee import TargetEmployee
from .Enemies.TargetManager import TargetManager
from .Enemies.Karen import Karen


class Target(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Lucas Smidt")
        enemies = ItemList(content_type=Enemy)
        enemies.add(TargetEmployee())
        enemies.add(TargetManager())
        enemies.add(Karen())
        super().__init__(
            "Target",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
