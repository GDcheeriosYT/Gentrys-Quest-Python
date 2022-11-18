# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class BrodyKrysa(Character):
    def __init__(self):
        super().__init__(
            "Brody Krysa",
            "Mighty warrior. Known as wall climber.",
            StarRating(1),
            None,
            None
        )
