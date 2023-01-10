# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Hands import Hands


class AmongUsCrewmate(Enemy):
    def __init__(self):
        super().__init__(
            "Among Us Crewmate",
            1,
            1,
            2,
            Hands(),
            "The average crewmate from Among Us has landed in Ohio to try and find the Imposter (DO NOT look sus or it may vote you out).",
            Experience()
        )
