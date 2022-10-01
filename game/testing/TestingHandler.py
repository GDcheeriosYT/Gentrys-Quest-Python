# game packages
# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText

# entity packages
from Entity.Character.Character import Character

class TestingHandler:
    """
    Creates an instance of a handler for testing game stuff
    """

    def __init__(self):
        pass

    @staticmethod
    def start():
        QuestionText("What shall we test today?").display()
        input()