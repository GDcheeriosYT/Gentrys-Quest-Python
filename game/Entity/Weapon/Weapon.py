# game packages
# entity packages
from ..Entity import Entity
from ..Stats.StarRating import StarRating
from ..Stats.Experience import Experience

class Weapon(Entity):
    """
    Makes a weapon

    parameters

    name: string
        the name of the Weapon

    description: string
        the description of the Weapon

    attack: int
        the attack damage that the Weapon does

    buff: Buff
        the attribute of the user to buff

    star_rating: StarRating
        the star rating of the Weapon

    experience: Experience
        the experience for the Weapon
    """

    name = None
    description = None
    attack = None
    buff = None
    star_rating = None
    experience = None

    def __init__(self, name, description="description", attack=0, buff=None, star_rating=StarRating(), experience=Experience()):
        super().__init__(self, name, description, star_rating, experience)
        self.attack = attack
        self.buff = buff