# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Stats.Experience import Experience

# content packages
from ..Weapons.Hands import Hands


class CourtesyClerk(Enemy):
    def __init__(self):
        super().__init__(
            "Courtesy Clerk",
            1,
            1,
            3,
            Hands(),
            "What is a Courtesy Clerk???",
            Experience()
        )
