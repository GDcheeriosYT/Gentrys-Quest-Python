# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Clipboard import Clipboard


class OshaWorker(Enemy):
    def __init__(self):
        super().__init__(
            "OSHA Worker",
            0,
            0,
            0,
            Clipboard(),
            "An OSHA worker with an unlimited supply of clipboards.",
            Experience()
        )
