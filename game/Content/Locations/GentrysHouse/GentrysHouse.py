# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea
from Location.Location import Location

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Weapon.Weapon import Weapon


class TestDummy(Enemy):
    def __init__(self):
        super().__init__(
            "Test Dummy",
            1,
            1,
            1,
            Weapon(),
            "A Test Dummy!"
        )


class GentrysHouse(BattleArea):
    def __init__(self, difficulty):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("GMoney")
        enemies = ItemList(content_type=Enemy)
        enemies.add(TestDummy)
        super().__init__(
            f"Gentry's House lvl{difficulty * 20}-{(difficulty * 20) + 19}",
            difficulty,
            artifact_families,
            enemies,
            True,
            False
        )


class GentrysHouseLocation(Location):
    def __init__(self):
        super().__init__(
            "Gentry's House",
            [
                GentrysHouse(0),
                GentrysHouse(1),
                GentrysHouse(2),
                GentrysHouse(3),
                GentrysHouse(4),
                GentrysHouse(5),
            ]
        )
