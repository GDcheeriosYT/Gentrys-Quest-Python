# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating

# content packages
import Content.Artifacts

# built-in packages
import importlib
import inspect
import os


class Family:
    def __init__(self, name):
        self.name = name
        self.artifacts = []
        self.buff = None


class ArtifactContentManager:
    def __init__(self):
        self.families = []

    def load_content(self):
        family_string = ""
        for module in vars(Content.Artifacts):
            family = None
            for hopefully_a_class in inspect.getmembers(module):
                #print(hopefully_a_class)
                if inspect.isclass(hopefully_a_class[1]):
                    if issubclass(hopefully_a_class[1], Artifact):
                        if family is None:
                            family = Family(hopefully_a_class[1]().family)

                        new_artifact = hopefully_a_class[1]()
                        family.artifacts.append(new_artifact)

            if family is not None:
                self.families.append(family)

        print(self.families)

    def get_families(self):
        return self.families
