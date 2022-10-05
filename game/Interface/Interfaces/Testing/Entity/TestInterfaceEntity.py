from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from .Artifact.TestArtifactInterface import TestArtifactInterface


class TestInterfaceEntity(Interface):
    def __init__(self):
        super().__init__("Welcome to the Test Entity Interface",
                         content=InterfaceContent("Meow this is some great info",
                                                  ["Artifact", "Character", "Enemy", "Weapon"]))

    def __repr__(self):
        action = self.visit()
        if action == 0:
            TestArtifactInterface().__repr__()  # Temporary
        elif action == 1:
            pass  # Temporary
        elif action == 2:
            pass  # Temporary
        elif action == 3:
            pass  # Temporary
