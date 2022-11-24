# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class JoeNuts(Character):
    def __init__(self):
        super().__init__(
            "Joe Nuts",
            "Massive man who likes sausage.",
            StarRating(4),
            None,
            None,
            default_defense_points=3
        )
