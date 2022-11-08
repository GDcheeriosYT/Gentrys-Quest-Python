# game packages
# collection packages
from Collection.Inventory.Inventory import Inventory

# config packages
from Config.NumberSetting import NumberSetting

# entity packages
from Entity.Character.Character import Character
from Entity.Artifact.Artifact import Artifact
from Entity.Weapon.Weapon import Weapon

# IO packages
from IO.Input import get_int
from IO import Window


class InventoryTestInterface:
    def __init__(self):
        self.inventory = Inventory(None)

    def change_money(self):
        money = NumberSetting("money", self.inventory.money, 0)
        money.change_value()
        self.inventory.money = money.value

    def add_character(self):
        self.inventory.character_list.characters.append(Character("Test Character", "just a test character."))

    def add_artifact(self):
        self.inventory.artifact_list.artifacts.append(Artifact("Test Artifact"))

    def add_weapon(self):
        self.inventory.weapon_list.weapons.append((Weapon("Test Weapon", "just a test weapon.")))

    def __repr__(self):
        while True:
            Window.clear()
            choice = get_int(
                "1. view inventory\n"
                "2. change money\n"
                "3. add character\n"
                "4. add artifact\n"
                "5. add weapon\n"
                "6. back"
            )

            if choice == 1:
                self.inventory.manage_input()

            elif choice == 2:
                self.change_money()

            elif choice == 3:
                self.add_character()

            elif choice == 4:
                self.add_artifact()

            elif choice == 5:
                self.add_weapon()

            else:
                raise TypeError
