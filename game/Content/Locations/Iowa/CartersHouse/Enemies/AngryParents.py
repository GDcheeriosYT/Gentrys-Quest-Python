# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Yelling import Yelling


class AngryParents(Enemy):
    def __init__(self):
        super().__init__(
            "Angry Parents Paul and Val",
            0,
            2,
            1,
            Yelling(),
            "Uh Oh, his parents are angry at him again.",
            Experience()
        )
