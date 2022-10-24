# game packages
# entity packages
from .Stats.StarRating import StarRating
from .Stats.Experience import Experience


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

    def level_up(self, amount):
        self.experience.level += amount
        try:
            self.update_stats()
        except:
            pass

    def add_xp(self, amount):
        difference = self.experience.get_xp_required(self.star_rating.value) - self.experience.xp
        still_upgrading = True
        while still_upgrading:
            if self.experience.xp + amount > self.experience.get_xp_required(self.star_rating.value):
                amount -= difference
                self.level_up(1)
                self.experience.xp = difference
                difference = self.experience.get_xp_required(self.star_rating.value) - self.experience.xp
            else:
                self.experience.xp += amount
                still_upgrading = False

    @staticmethod
    def check_minimum(variable, multiplier=1, subtract_one_true=False):
        if variable < 1:
            return 1 if not subtract_one_true else 0
        else:
            return variable * multiplier
