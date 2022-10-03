# game packages
# IO packages
from IO import Window

# Interface packages
from .InterfaceContent import InterfaceContent

# Graphics packages
from Graphics.Text.Text import Text
from Graphics.Content.Text.WarningText import WarningText

# external packages
from rich.console import Console


class Interface:
    """
    makes an interface in game

    parameters
    title: string
        the title of the interface

    is_rule: boolean
        if it will display as a rule

    content: dict
        the content of the interface
    """

    title = None
    is_rule = None

    def __init__(self, title="interface", is_rule=False, content=InterfaceContent()):
        self.title = title
        self.is_rule = is_rule
        self.content = content

    def choose(self, selection):
        selection = selection - 1
        return self.content.options[selection]

    def visit(self, clear_window=True):
        visiting = True
        while visiting:
            if clear_window:
                Window.clear()
            if self.is_rule:
                Console().rule(self.title)
            else:
                Text(self.content.info).display()
                try:
                    selection = int(input(self.content.show_options()))
                    visiting = False
                    self.choose(selection)
                except ValueError:
                    WarningText(f"Nope!").display()
