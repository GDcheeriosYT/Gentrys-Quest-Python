# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.YiLongMa import YiLongMa


class BeiJing(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Brayden Messerschmidt")
        artifact_families.add("Carter Ballard")
        enemies = ItemList(content_type=Enemy)
        enemies.add(YiLongMa())
        super().__init__(
            "Beijing (北京)",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
