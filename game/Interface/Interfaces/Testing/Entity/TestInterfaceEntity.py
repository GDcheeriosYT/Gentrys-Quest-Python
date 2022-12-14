from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from .Artifact.TestArtifactInterface import TestArtifactInterface
from .Weapon.TestWeaponInterface import TestWeaponInterface
from .Character.TestCharacterInterface import TestCharacterInterface
from .Enemy.TestInterfaceEnemy import TestInterfaceEnemy

class TestInterfaceEntity(Interface):
    def __init__(self):
        super().__init__("Welcome to the Test Entity Interface",
                         content=InterfaceContent("Meow this is some great info",
                                                  ["Artifact", "Character", "Enemy", "Weapon"]))

    def __repr__(self):
        action = self.visit()
        if action == 0:
            test_interface = TestArtifactInterface()
            while True:
                try:
                    test_interface.__repr__()
                except TypeError:
                    break
        elif action == 1:
            test_interface = TestCharacterInterface()
            while True:
                try:
                    test_interface.__repr__()
                except TypeError as e:
                    print(e)
                    break
        elif action == 2:
            test_interface = TestInterfaceEnemy()
            while True:
                try:
                    test_interface.__repr__()
                except TypeError:
                    break
        elif action == 3:
            test_interface = TestWeaponInterface()
            while True:
                try:
                    test_interface.__repr__()
                except TypeError:
                    break
