# game packages
# interface packages
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent
from .BattleArea.BattleAreaTestInterface import BattleAreaTestInterface


class LocationInterface(Interface):
    def __init__(self):
        super().__init__("Welcome to the Test Location Interface",
                         content=InterfaceContent("Meow this is some great info",
                                                  ["BattleArea"]))

    def __repr__(self):
        action = self.visit()
        if action == 1:
            test_interface = BattleAreaTestInterface()
