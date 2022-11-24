# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class RyanMartinez(Character):
    def __init__(self):
        super().__init__(
            "Ryan Martinez",
            "An American former YouTuber known for his rant videos, vlogs, and for being a superfan of the American football team the Philadelphia Eagles.",
            StarRating(2),
            None,
            None,
            default_health_points=1
        )
