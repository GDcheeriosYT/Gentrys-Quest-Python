from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent


class TravelInterface(Interface):
    def __init__(self):
        super().__init__("", False, InterfaceContent("Where will you go?", ["no locations..."]))

    def __repr__(self):
        action = self.visit()
        if action == InterfaceContent.options[0]:
            print("no locations homie")
