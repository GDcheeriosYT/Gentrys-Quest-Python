# graphics packages
from .Style import Style

# external packages
from rich.console import Console

class Text:
    """
    Makes text for the game

    parameters

    content: string
        the content of the text

    style: Style
        the style of the text
    """

    content = None
    style = None

    def __init__(self, content="text", style=Style("black", "white")):
        self.content = content
        self.style = style

    def display(self):
        Console().print(f"{self.style}{self.content}")
