# game packages
# graphics packages
from Graphics.Content.Text.WarningText import WarningText

# IO packages
from IO import Window

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

    def __init__(self, size=None, content_type=None, fill=False, output=True):
        self.content = []
        self.size = size
        if fill and size is not None:
            for i in range(size):
                self.content.append(None)
        self.content_type = content_type
        self.output = output

    def add(self, item):
        if self.check_item_and_space(item):
            self.content.append(item)
        else:
            for thing in self.content:
                if thing is None:
                    self.content[self.content.index(thing)] = item
                    return None
            if self.output:
                WarningText(
                    f"The {type(item)} {item.name} isn't accepted in this list. \nEither it's full or it doesn't accept {type(item)}").display()

    def remove(self):
        for item in self.content:
            Console().print(f"{self.content.index(item) + 1}. {item}")

        selection = input("which item would you like to remove?\n")
        try:
            return self.content.pop(self.content.index(int(selection) - 1))
        except IndexError:
            WarningText(f"Couldn't find item at {selection}").display()

    def fill(self, list):
        for item in list:
            self.add(item)

    def get(self, index):
        try:
            return self.content[index]
        except IndexError:
            return None

    def check_item_and_space(self, item):
        if isinstance(item, self.content_type) or self.content_type is None:
            if self.size is not None:
                if len(self.content) < self.size:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def set(self, index, item):
        try:
            if self.check_item_and_space(item):
                self.content[index] = item
            else:
                WarningText(
                    f"The {type(item)} {item} isn't accepted in this list. \nEither it's full or it doesn't accept {type(item)}").display()
        except IndexError:
            WarningText(f"Can't put that here").display()

    def test(self):
        while True:
            try:
                Window.clear()
                counter = 1
                for item in self.content:
                    print(f"{counter}. {item}")
                    counter += 1
                print(f"{counter}. back")
                num = int(input())
                if self.content[num - 1] is None:
                    self.content[num - 1] = self.content_type("Test Item")
                    self.content[num - 1] = self.content[num - 1].test()
                else:
                    self.content[num - 1] = self.content[num - 1].test()
            except ValueError:
                Window.clear()
                WarningText("Not a number!").display()
            except NameError:
                WarningText("Couldn't find a test method for this class").display()
                break
            except IndexError:
                break

    def delete_after(self, index):
        x = len(self.content) - 1
        while x != index:
            self.content[x].pop()
            x -= 1

    def change_limit(self, amount):
        Window.clear()
        if amount < self.size:
            WarningText(
                "You are lowering the size.\nThis could permanently delete stuff.\nAre you sure you want to continue?\n").display()
            try:
                num = int(input("1. yes\n2. no"))
                if num == 1:
                    self.size = amount
                    self.delete_after(self.size)
            except ValueError:
                WarningText("mans didn't even put a number...").display()

    def __repr__(self):
        return {
            "size": self.size,
            "content type": self.content_type,
            "content": self.content
        }
