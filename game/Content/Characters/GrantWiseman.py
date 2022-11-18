# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class GrantWiseman(Character):
    def __init__(self):
        super().__init__(
            "Grant Wiseman",
            "Large and made of shit.",
            StarRating(1),
            None,
            None
        )
