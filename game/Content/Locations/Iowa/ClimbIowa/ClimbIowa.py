# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.GymBro import GymBro
from .Enemies.EightYearOldWhoCanClimbV9s import EightYearOldWhoClimbV9s


class ClimbIowa(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Brody Krysa")
        artifact_families.add("David Napier")
        enemies = ItemList(content_type=Enemy)
        enemies.add(GymBro())
        enemies.add(EightYearOldWhoClimbV9s())
        super().__init__(
            "Climb Iowa",
            0,
            artifact_families,
            enemies,
            True,
            True
        )