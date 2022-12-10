# game packages
# entity packages
from Entity.Character.Character import Character

# built-in packages
import importlib
import inspect
import os


class CharacterContentManager:
    families = None

    def __init__(self):
        families = []

    @staticmethod
    def get_content():
        characters = []
        for character_file in os.listdir("Content/Characters"):
            character_file = character_file[
                             :-3]  # removing the ".py" so it can be treated as an actual package for import
            if character_file[0] != "_":
                character_class = importlib.import_module(f".{character_file}", f"Content.Characters")
                for thing in inspect.getmembers(character_class):
                    thing = thing[1]
                    if inspect.isclass(thing):
                        if issubclass(thing, Character):
                            characters.append(thing)

        return characters
