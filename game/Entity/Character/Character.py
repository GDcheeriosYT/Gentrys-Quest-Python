# game packages
# entity packages
from ..Entity import Entity
from ..Weapon.Weapon import Weapon
from ..Stats.StarRating import StarRating
from ..Stats.Experience import Experience
from ..Artifact.Artifact import Artifact

# collection packages
from Collection.ItemList import ItemList


class Character(Entity):
    """
    Makes a Character class

    parameters

    name: string
        the name of the Character

    description: string
        the description of the Character

    star_rating: int
        the star rating of the Character

    experience: Experience
        the experience of the Character

    weapon: Weapon
        the Weapon that the Character has equipped

    artifacts: ItemList
        the Artifacts that the character has

    default_health_points: int
        the default health points the Character has

    default_attack_points: int
        the default attack points damage that the Character does

    default_defense_points: int
        the default defense points that the Character has

    default_crit_rate_points: int
        the default crit rate points the Character has

    default_crit_damage_points: int
        the default crit damage points the character has
    """

    name = None
    description = None
    star_rating = None
    experience = None
    weapon = None
    artifacts = None
    default_health = None
    default_attack = None
    default_defense = None
    default_crit_rate = None
    default_crit_damage = None
    difficulty = None

    def __init__(self, name, description="description", star_rating=StarRating(1), experience=Experience(), weapon=None,
                 artifacts=ItemList(5, Artifact), default_health_points=0, default_attack_points=0,
                 default_defense_points=0, default_crit_rate_points=0,
                 default_crit_damage_points=0):
        super().__init__(name, description, star_rating, experience)
        self.weapon = weapon
        self.artifacts = artifacts
        self.default_health = (2 * self.experience.level + (self.star_rating * 10))
        self.default_attack = int(((self.experience.level * 1.45) + self.star_rating + 2))
        self.default_defense = int((self.experience.level * 0.2) + self.star_rating)
        self.default_crit_rate = int(6 + (self.experience.level * 0.2) + self.star_rating)
        self.default_crit_damage = int((self.experience.level * 1.45) + self.star_rating + 2)
        self.difficulty = int(1 + (self.experience.level / 20))
