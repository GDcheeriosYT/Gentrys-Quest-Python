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

    text_animation: TextAnimation
        the text animation
    """

    content = None
    style = None
    text_animation = None

    def __init__(self, content="text", style=Style("black", "white")):
        self.content = content
        self.style = style

    def display(self, same_line=False):
        Console().print(f"{self.style}{self.content}", end='\r' if same_line else '\n')

    def raw_output(self):
        return f"{self.style}{self.content}"
