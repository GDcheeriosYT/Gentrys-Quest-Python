# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy


class BraydensHouse(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Brayden Messerschmidt")
        artifact_families.add("Dan Messerschmidt")
        enemies = ItemList(content_type=Enemy)

        super().__init__(
            "Brayden's House",
            0,

        )
