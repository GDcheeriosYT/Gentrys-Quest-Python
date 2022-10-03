from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from .Travel.TravelInterface import TravelInterface


class PlayInterface(Interface):
    def __init__(self):
        super().__init__("", False, InterfaceContent("what will you do?", ["travel", "inventory"]))

    def __repr__(self):
        action = self.visit()
        if action == InterfaceContent.options[0]:
            TravelInterface()
