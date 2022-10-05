# game packages
# entity packages
from .StatTypes import StatTypes
from .Experience import Experience

# built-in packages
import random


class Buff:
    """
    Makes a buff for attributes

    parameters

    attribute_type: StatTypes
        the attribute for the buff to buff

    experience: Experience
        the experience of the buff

    is_percent: boolean
        determines if the buff is a percent type
    """

    attribute_type = None
    experience = None
    is_percent = None

    def __init__(self, attribute_type=random.choice(list(StatTypes)), experience=Experience, is_percent=random.choice([True, False])):
        self.attribute_type = attribute_type
        self.experience = experience
        self.is_percent = is_percent

    def __repr__(self):
        return f"{self.attribute_type.name} 0{'%' if self.is_percent else ''}"
