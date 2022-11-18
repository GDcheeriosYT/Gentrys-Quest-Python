# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class MatheuSliger(Character):
    def __init__(self):
        super().__init__(
            "Matheu Sliger",
            "Big Ninja.",
            StarRating(1),
            None,
            None
        )
