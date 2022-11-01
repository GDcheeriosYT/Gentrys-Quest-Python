from Graphics.Text.Text import Text
from Graphics.Text.Style import Style


# external packages

class Difficulty:
    """
    the difficulty of a battle area

    parameters

    value: int
        the value of the difficulty
    """

    value = None

    def __init__(self, value=1):
        self.value = value

    def __repr__(self):
        string = ""
        for _ in range(self.value):
            string += "⚠"
        return Text(string).raw_output()
