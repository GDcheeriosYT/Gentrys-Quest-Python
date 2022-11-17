# game packages
# interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent
from Interface.Interfaces.Testing.Location.BattleAreaTestInterface import BattleAreaTestInterface


class LocationInterface(Interface):
    def __init__(self):
        super().__init__("Welcome to the Test Location Interface",
                         content=InterfaceContent("Meow this is some great info",
                                                  ["BattleArea"]))

    def __repr__(self):
        action = self.visit()
        if action == 0:
            test_interface = BattleAreaTestInterface()
            while True:
                try:
                    test_interface.__repr__()
                except TypeError:
                    break
