from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent
from .SingleplayerInterface import SingleplayerInterface

from .Travel.TravelInterface import TravelInterface


class PlayInterface(Interface):
    def __init__(self, data):
        super().__init__("", False, InterfaceContent("what will you do?", ["singleplayer", "multiplayer"]))

    def __repr__(self):
        action = self.visit()
        if action == 0:
            SingleplayerInterface.__repr__()
        elif action == 1:
            print("not available yet")
