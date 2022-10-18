# game packages
# entity packages
from ..Entity import Entity
from ..Stats.StarRating import StarRating
from ..Stats.Experience import Experience
from ..Stats.StatTypes import StatTypes
from ..Stats.Buff import Buff


class Weapon(Entity):
    """
    Makes a weapon

    parameters

    name: string
        the name of the Weapon

    description: string
        the description of the Weapon

    weapon_type: string
        the weapon type

    attack: int
        the attack damage that the Weapon does

    buff: Buff
        the attribute of the user to buff

    verbs: Verbs
        the verbs to be used by the weapon

    star_rating: StarRating
        the star rating of the Weapon

    experience: Experience
        the experience for the Weapon
    """

    name = None
    description = None
    weapon_type = None
    attack = None
    buff = None
    verbs = None
    star_rating = None
    experience = None

    def __init__(self, name="fists", description="punches things", weapon_type=None, attack=3,
                 buff=Buff(StatTypes.Health, Experience(), False), verbs=None, star_rating=StarRating(), experience=Experience()):
        super().__init__(name, description, star_rating, experience)
        self.weapon_type = weapon_type
        self.attack = attack
        self.buff = buff
        self.verbs = verbs

    def __repr__(self):
        return (
f"""
{self.name} {self.star_rating} {self.experience}
"meow " type: {self.weapon_type}
base attack: {self.attack}
attribute: {self.buff}
"""
        )
