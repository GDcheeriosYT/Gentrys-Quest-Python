# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class ConnorFogarty(Character):
    def __init__(self):
        super().__init__(
            "Connor Fogarty",
            "A mutant shih tzu who loves cheese and belly rubs.",
            StarRating(3),
            None,
            None,
            default_attack_points=1,
            default_defense_points=1
        )
