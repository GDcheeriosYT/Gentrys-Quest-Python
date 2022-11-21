# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.SharpPencil import SharpPencil


class FlyingPencil(Enemy):
    def __init__(self):
        super().__init__(
            "Flying Pencil",
            0,
            2,
            0,
            SharpPencil(),
            "Wait... Does that pencil have wings?",
            Experience()
        )
