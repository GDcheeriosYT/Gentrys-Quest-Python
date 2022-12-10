# game packages
# entity packages
from Entity.Character.Character import Character

# built-in packages
import importlib
import inspect
import os

# graphics packages
from Graphics.Status import Status

from Content.Characters import *


class CharacterContentManager:
    characters = None

    def __init__(self):
        self.characters = []

    def load_content(self):
        load_status = Status("Loading Game Characters...")
        load_status.start()
        for module in globals().values():
            if inspect.ismodule(module):
                if module.__name__.startswith("Content.Characters."):
                    for hopefully_a_class in vars(module).values():
                        if inspect.isclass(hopefully_a_class):
                            if (issubclass(hopefully_a_class, Character)) and not (
                                    hopefully_a_class.__name__ == "Character"):
                                self.characters.append(hopefully_a_class)

        load_status.stop()

    def get_characters(self):
        return self.characters
