# game packages
# entity packages
from ..Entity import Entity
from ..Stats.Buff import Buff
from ..Stats.Experience import Experience
from ..Stats.StarRating import StarRating

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# collection packages
from Collection.ItemList import ItemList

# config packages
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager


class Artifact(Entity):
    """
    Makes an artifact

    parameters

    name: string
        the name of the Artifact

    star_rating: StarRating
        the star rating of the Artifact

    family: ArtifactFamily
        the family that the Artifact is in

    main_attribute: Buff
        the main attribute of the Artifact

    attributes: list
        the attributes that this artifact has

    experience: Experience
        the experience of the Artifact
    """

    name = None
    star_rating = None
    family = None
    main_attribute = None
    attributes = None
    experience = None

    def __init__(self, name, star_rating=StarRating(), family=None, main_attribute=Buff(), attributes=[],
                 experience=Experience()):
        super().__init__(name=name, description="description", star_rating=star_rating, experience=experience)
        self.family = family
        self.main_attribute = main_attribute
        self.attributes = attributes
        self.settings = [
            StringSetting("name", self.name),
            NumberSetting("star rating", self.star_rating.value, 1, 5),
            StringSetting("family", self.family),
            ClassSetting("main attribute", self.main_attribute),
            NumberSetting("level", self.experience.level)
        ]

    def display_attributes(self):
        string = "\n"
        for attribute in self.attributes:
            string += f"{attribute}\n"

        return string

    def __repr__(self):
        return (
            f"""
=========================================
{self.name} {self.star_rating} {self.experience}
apart of the {self.family} family
* {self.main_attribute} *
{f"attributes{self.display_attributes()}" if len(self.attributes) > 0 else ""}
=========================================
"""
        )

    def test(self):
        self.settings = SettingManager(self.settings).config_settings(False)
