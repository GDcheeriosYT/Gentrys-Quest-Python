# game packages
# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText

# entity packages
from Entity.Character.Character import Character

# interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Interface.Interfaces.Testing.Entity.TestInterfaceEntity import TestInterfaceEntity

class TestingHandler:
    """
    Creates an instance of a handler for testing game stuff
    """

    def __init__(self):
        pass

    @staticmethod
    def start():
        QuestionText("What area shall we test today? (Meow:))").display()
        in_game = True
        while in_game:
            choices = int(input("1. Entity\n"
                                "2. quit\n"))

            if choices == 1:
                TestInterfaceEntity().__repr__()
            elif choices == 2:
                SettingsInterface(game_data.settings).__repr__()
            else:
                in_game = False
