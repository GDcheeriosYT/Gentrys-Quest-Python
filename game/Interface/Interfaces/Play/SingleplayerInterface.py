from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from .Travel.TravelInterface import TravelInterface


class SingleplayerInterface(Interface):
    def __init__(self, data):
        super().__init__("", False, InterfaceContent("what will you do?", ["travel", "inventory"]))
        self.data = data

    def __repr__(self):
        action = self.visit()
        if action == 0:
            TravelInterface().__repr__()
        elif action == 1:
            print(self.data)

