# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating

# content packages
from Content.Artifacts import *

# graphics packages
from Graphics.Status import Status

# built-in packages
import inspect


class Family:
    def __init__(self, name):
        self.name = name
        self.artifacts = []
        self.buff = None


class ArtifactContentManager:
    def __init__(self):
        self.families = []

    def load_content(self):
        load_status = Status("Loading Game Artifacts...")
        family_string = ""
        load_status.start()
        for module in globals().values():
            family = None
            if inspect.ismodule(module):
                if module.__name__.startswith("Content.Artifacts."):
                    for hopefully_a_class in vars(module).values():
                        if inspect.isclass(hopefully_a_class):
                            if (issubclass(hopefully_a_class, Artifact)) and not (hopefully_a_class.__name__ == "Artifact"):
                                if family is None:
                                    family = Family(hopefully_a_class(StarRating()).family)

                                new_artifact = hopefully_a_class
                                family.artifacts.append(new_artifact)

                    if family is not None:
                        self.families.append(family)

        load_status.stop()

    def get_families(self):
        return self.families
