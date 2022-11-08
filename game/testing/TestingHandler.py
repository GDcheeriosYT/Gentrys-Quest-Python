# game packages
# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText

# entity packages
from Entity.Character.Character import Character

# interface packages
from Interface.Interfaces.Testing.Entity.TestInterfaceEntity import TestInterfaceEntity
from Interface.Interfaces.Testing.Location.LocationInterface import LocationInterface
from Interface.Interfaces.Testing.Inventory.InventoryInterface import InventoryInterface

# IO packages
from IO import Window
from IO.Input import get_int


class TestingHandler:
    """
    Creates an instance of a handler for testing game stuff
    """

    def __init__(self):
        pass

    @staticmethod
    def start():
        while True:
            entity_interface = TestInterfaceEntity()
            location_interface = LocationInterface()
            inventory_interface = InventoryInterface()
            Window.clear()
            QuestionText("What area shall we test today? (Meow:))").display()
            choices = get_int("1. Entity\n"
                              "2. Inventory\n"
                              "3. Location\n"
                              "4. quit\n")
            if choices == 1:
                entity_interface.__repr__()

            elif choices == 2:
                inventory_interface.__repr__()

            elif choices == 3:
                location_interface.__repr__()

            else:
                break

