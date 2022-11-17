# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Camera(Weapon):
    def __init__(self):
        super().__init__(
            "Camera",
            "A regular IPhone camera.",
            "Trident",
            0,
            Buff(),
            Verbs("recorded", "left a bad review about"),
            StarRating(5),
            Experience()
        )
