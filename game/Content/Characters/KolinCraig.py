# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class KolinCraig(Character):
    def __init__(self):
        super().__init__(
            "Kolin Craig",
            "A super *tall* and handsome man.",
            StarRating(3),
            None,
            None,
            default_health_points=1,
            default_defense_points=1
        )
