# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating

# built-in packages
import importlib
import inspect
import os


class Location:
    def __init__(self, name):
        self.name = name
        self.areas = []


class LocationContentManager:
    families = None

    def __init__(self):
        self.locations = []

    @staticmethod
    def load_content():
        locations = []
        for location in os.listdir("Content/Locations"):
            location = location[:-3]  # removing the ".py" so it can be treated as an actual package for import
            if family[0] != "_":
                family_class = importlib.import_module(f".{family}", f"Content.Locations")
                new_family = None
                for thing in inspect.getmembers(family_class):
                    thing = thing[1]
                    if inspect.isclass(thing):
                        if issubclass(thing, Artifact):
                            try:
                                thing_for_family = thing(StarRating(0))
                                if thing_for_family.family is not None:
                                    if new_family is None:
                                        new_family = Family(thing_for_family.family)
                                    new_family.artifacts.append(thing)
                            except TypeError as e:
                                print(f"uh oh...\n{e}")
                if new_family is not None:
                    families.append(new_family)

        return families