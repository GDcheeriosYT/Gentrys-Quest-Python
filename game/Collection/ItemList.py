# game packages
# graphics packages
from ..Graphics.Content.Text.WarningText import WarningText

# external packages
from rich.console import Console

class ItemList:
    """
    Makes an ItemList

    an ItemList is a special type of list. It can have a specified size and a specified type of "thing".
    say you want to hold a maximum of 8 tacos. It will only allow for 8 things of the type Taco.

    parameters

    size: int
        the maximum size of the list

    content_type: class type
        the content that will be filled in the list
    """

    size = None
    content_type = None

    def __init__(self, size=None, content_type=None):
        self.content = []
        self.size = size
        self.content_type = content_type

    def add(self, item):
        if (len(self.content) < self.size or self.size is None) and (type(item) == type(self.content_type) or self.content_type is None):
            self.content.append(item)
        else:
            WarningText(f"This list either is full or doesn't accept {type(item)}").display()

    def remove(self):
        for item in self.content:
            Console().print(f"{self.content.index(item) + 1}. {item}")

        selection = input("which item would you like to remove?\n")
        try:
            return self.content.pop(self.content.index(int(selection) - 1))
        except:
            WarningText(f"Couldn't find item at {selection}").display()

    def __repr__(self):
        return {
            "size": self.size,
            "content type": self.content_type,
            "content": self.content
        }
