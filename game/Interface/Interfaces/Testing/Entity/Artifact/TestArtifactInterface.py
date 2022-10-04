from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Entity.Artifact.Artifact import Artifact



class TestArtifactInterface(Interface):
    def __init__(self, artifact=Artifact("")):
        super().__init__("Artifact stuff", content=InterfaceContent("Meow this is some great info", ["Artifact", "Character", "Enemy", "Weapon"]))

    def __repr__(self):
        action = self.visit()
        if action == 0:
            InterfaceContent # Temporary
        elif action == 1:
            InterfaceContent # Temporary
        elif action == 2:
            InterfaceContent # Temporary
        elif action == 3:
            InterfaceContent # Temporary


