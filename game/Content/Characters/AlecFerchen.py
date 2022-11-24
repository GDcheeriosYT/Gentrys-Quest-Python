# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class AlecFerchen(Character):
    def __init__(self):
        super().__init__(
            "Alec Ferchen",
            "Big Sexy Man",
            StarRating(3),
            None,
            None,
            default_attack_points=2
        )
