# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class DavidNapier(Character):
    def __init__(self):
        super().__init__(
            "David Napier",
            "6'4''.",
            StarRating(1),
            None,
            None
        )
