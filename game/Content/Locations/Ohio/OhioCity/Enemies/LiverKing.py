# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.LiverBoostedHands import LiverBoostedHands


class LiverKing(Enemy):
    def __init__(self):
        super().__init__(
            "Liver King",
            3,
            2,
            2,
            LiverBoostedHands(),
            "Brian Johnson's alter ego Liver King actually lives in Ohio.",
            Experience()
        )
