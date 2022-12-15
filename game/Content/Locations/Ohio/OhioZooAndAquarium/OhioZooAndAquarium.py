# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.HarambesCousin import HarambesCousin
from .Enemies.FishNamedBryan import FishNamedBryan
from .Enemies.BabyDragon import BabyDragon


class OhioZooAndAquarium(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Ohio's Zoo & Aquarium")
        enemies = ItemList(content_type=Enemy)
        enemies.add(HarambesCousin())
        enemies.add(FishNamedBryan())
        enemies.add(BabyDragon())
        super().__init__(
            "Ohio's Zoo & Aquarium",
            0,
            artifact_families,
            enemies,
            True,
            True
        )