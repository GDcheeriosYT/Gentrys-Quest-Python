# game packages
# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText

# entity packages
from Entity.Character.Character import Character

# interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Interface.Interfaces.Testing.Entity.TestInterfaceEntity import TestInterfaceEntity

# IO packages
from IO import Window

class TestingHandler:
    """
    Creates an instance of a handler for testing game stuff
    """

    def __init__(self):
        pass

    @staticmethod
    def start():
        while True:
            entity_interface = TestInterfaceEntity()
            Window.clear()
            QuestionText("What area shall we test today? (Meow:))").display()
            choices = int(input("1. Entity\n"
                                "2. quit\n"))

            if choices == 1:
                entity_interface.__repr__()
            else:
                break
