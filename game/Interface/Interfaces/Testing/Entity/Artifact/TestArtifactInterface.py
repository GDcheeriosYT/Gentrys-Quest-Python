from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

from Random.Functions import get_random_name

from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting

import random

class TestArtifactInterface(Interface):

    artifact = None

    def __init__(self, level=1, star_rating=1, main_attribute=Buff(), attributes=[]):
        self.artifact=Artifact(get_random_name(False), StarRating(star_rating), None, Buff(), [], Experience())
        super().__init__("Artifact stuff", content=InterfaceContent(self.artifact, ["nothing yet..."]))
        
    def __repr__(self):
        action = self.visit()

