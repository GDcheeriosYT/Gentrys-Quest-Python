# game packages
# entity packages
from StatTypes import StatTypes
from Experience import Experience

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
    """

    attribute_type = None
    experience = None

    def __init__(self, attribute_type=random.choice(list(StatTypes)), experience=Experience):
        self.attribute_type = attribute_type
        self.experience = experience
