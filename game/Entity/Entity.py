# game packages
#entity packages
from game.Entity.Stats.StarRating import StarRating

# external packages

class Entity:
    """
    makes an Entity

    parameters

    name: string
        the name of the Entity

    description: string
        the description of the Entity

    star_rating: StarRating
        the star rating of the Entity

    xp: int
        the xp of the Entity

    xp_required: int
        the xp required to level up the Entity

    level: int
        the level of the Entity
    """

    name = None
    description = None
    star_rating = None
    xp = None
    xp_required = None
    level = None

    def __init__(self, name, description="description", star_rating=StarRating(1), xp=0, xp_required=0, level=1):
        self.name = name
        self.description = description
        self.star_rating = star_rating
        self.xp = xp
        self.xp_required = xp_required
        self.level = level