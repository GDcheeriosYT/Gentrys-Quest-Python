# game packages
# IO packages
from IO import Window

# Interface packages
from .InterfaceContent import InterfaceContent

# Graphics packages
from Graphics.Text.Text import Text

#external packages
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

    def visit(self):
        Window.clear()
        if self.is_rule:
            Console().rule(self.title)
        else:
            Text(self.content.info).display()
            input(self.content.show_options())