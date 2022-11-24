# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class OliviaMesserschmidt(Character):
    def __init__(self):
        super().__init__(
            "Olivia Messerschmidt",
            "Creative.",
            StarRating(5),
            None,
            None,
            default_health_points=4
        )
