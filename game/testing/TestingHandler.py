# game packages
# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText

# entity packages
from Entity.Character.Character import Character

# interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent


class TestingHandler:
    """
    Creates an instance of a handler for testing game stuff
    """

    def __init__(self):
        pass

    @staticmethod
    def start():
        QuestionText("What area shall we test today?").display()
        Interface("", content=InterfaceContent("", ["player", "entity"])).visit(False)
