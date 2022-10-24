# game packages
# IO packages
from . import Window


def get_int(text):
    Window.clear()
    while True:
        try:
            num = int(input(text + "\n"))
            Window.clear()
            return num
        except ValueError:
            Window.clear()


def get_string(text):
    Window.clear()
    string = input(text + "\n")
    Window.clear()
    return string


def enter_to_continue():
    input("press enter to continue...\n")
