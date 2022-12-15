# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.ImpostersKnife import ImpostersKnife


class AmongUsImposter(Enemy):
    def __init__(self):
        super().__init__(
            "Among Us Imposter",
            2,
            3,
            2,
            ImpostersKnife(),
            "The Imposter from Among Us has come to Ohio to claim more lives.",
            Experience()
        )
