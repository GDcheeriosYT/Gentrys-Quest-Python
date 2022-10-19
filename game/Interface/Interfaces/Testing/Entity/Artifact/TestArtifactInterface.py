from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience
from Entity.Stats.Buff import Buff

from Graphics.Text.Text import Text

from Random.Functions import get_random_name

from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

from IO import Window

class TestArtifactInterface:

    artifact = None
    settings = None

    def __init__(self, level=1, star_rating=1, main_attribute=Buff(), attributes=[]):
        name = get_random_name(False)
        experience = Experience(level)
        self.artifact = Artifact(name, StarRating(star_rating), None, Buff(), [], Experience())
        self.artifact.experience.limit = self.artifact.star_rating.value*4
        self.settings = [
            StringSetting("name", name),
            NumberSetting("star rating", star_rating, 1, 5),
            StringSetting("family", self.artifact.family),
            ClassSetting("main attribute", self.artifact.main_attribute),
            NumberSetting("level", experience.level, 1, experience.limit)
        ]

    def __repr__(self):
        Window.clear()
        Text(self.artifact).display()
        self.settings = SettingManager(self.settings).config_settings()
        self.artifact.name = self.settings[0].text
        self.artifact.star_rating = StarRating(self.settings[1].value)
        self.artifact.experience.limit = self.artifact.star_rating.value*4
        self.artifact.family = self.settings[2].text
        self.artifact.main_attribute = self.settings[3].instance_class
        self.artifact.experience.level = self.settings[4].value
        self.settings[4] = NumberSetting("level", self.artifact.experience.level, 1, self.artifact.experience.limit)
        return self
