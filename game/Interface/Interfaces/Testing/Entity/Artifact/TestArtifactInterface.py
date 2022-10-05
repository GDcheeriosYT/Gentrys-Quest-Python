from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes

from Random.Functions import get_random_name

import random

class TestArtifactInterface(Interface):
    def __init__(self, artifact=Artifact(get_random_name(False), StarRating(random.randint(1, 5)), None, Buff(), [], Experience())):
        super().__init__("Artifact stuff", content=InterfaceContent(artifact, ["nothing yet..."]))
        self.artifact = artifact
        
    def __repr__(self):
        action = self.visit()

