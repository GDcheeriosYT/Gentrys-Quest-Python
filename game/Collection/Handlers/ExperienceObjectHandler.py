# game packages
# entity packages
from Entity.Stats.Experience import Experience


class ExperienceObjectHandler:
    """
    Makes a Handler for experience arrays

    parameters

    experience_object: list
        the object to handle
    """

    experience_object = None

    def __init__(self, experience_object: dict):
        self.experience_object = experience_object

    def create_experience(self):
        return Experience(
            self.experience_object["level"],
            self.experience_object["xp"],
        )
