# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.GorillaHands import GorillaHands


class HarambesCousin(Enemy):
    def __init__(self):
        super().__init__(
            "Harambe's Cousin Bennifer",
            4,
            2,
            1,
            GorillaHands(),
            "Harambe's Cousin Bennifer somehow lives on Ohio.",
            Experience()
        )
