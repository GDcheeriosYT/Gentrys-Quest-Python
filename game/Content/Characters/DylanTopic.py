# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class DylanTopic(Character):
    def __init__(self):
        super().__init__(
            "Dylan Topic",
            "Cool uhm uhm uhm uhm uhm uhm oh tetris dude.",
            StarRating(4),
            None,
            None,
            default_health_points=3
        )
