# game packages
#entity packages
from Stats.StarRating import StarRating
from Stats.Experience import Experience

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

    experience: Experience
        the experience of the Entity
    """

    name = None
    description = None
    star_rating = None
    experience = None

    def __init__(self, name, description="description", star_rating=StarRating(1), experience=Experience()):
        self.name = name
        self.description = description
        self.star_rating = star_rating
        self.experience = experience
