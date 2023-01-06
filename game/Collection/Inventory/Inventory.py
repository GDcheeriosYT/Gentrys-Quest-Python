# game packages
# collection packages
from .ArtifactList import ArtifactList
from .CharacterList import CharacterList
from .WeaponList import WeaponList

# graphics packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText
from Graphics.Text.Text import Text

# IO packages
from IO.Input import get_int

# entity packages
from Entity.Artifact.Artifact import Artifact

# built-in packages
from copy import deepcopy

class Inventory:
    """
    Holds all the users owned items

    returns an Inventory

    parameters

    inventory_data: json object
        data used to construct inventory
    """

    inventory_data = None
    character_list = None
    artifact_list = None
    weapon_list = None
    money = None

    def __init__(self, inventory_data):
        if inventory_data is None:
            inventory_data = {
                "money": 0,
                "characters": [],
                "weapons": [],
                "artifacts": []
            }

        self.money = inventory_data["money"]
        self.character_list = CharacterList(inventory_data["characters"]).give_item_list()
        self.weapon_list = WeaponList(inventory_data["weapons"]).give_item_list()
        self.artifact_list = ArtifactList(inventory_data["artifacts"]).give_item_list()

    def upgrade(self):
        pass

    def manage_input(self, equipped_character=None):
        def is_not_empty(list, string):
            if len(list) != 0:
                return True
            else:
                WarningText(f"You don't have any {string}s").display()

        while True:
            try:
                num = get_int(self.__repr__())
                if num == 1:
                    if is_not_empty(self.character_list.content, "character"):
                        equipped_character = self.manage_character(self.character_list.select(remove=False))
                elif num == 2:
                    if is_not_empty(self.weapon_list.content, "weapon"):
                        self.manage_weapon(self.weapon_list.select(remove=False))
                elif num == 3:
                    if is_not_empty(self.artifact_list.content, "artifact"):
                        self.manage_artifact(self.artifact_list.select(remove=False))
                else:
                    break
            except IndexError:
                break

        return equipped_character

    def can_afford(self, amount):
        if self.money >= amount:
            return True
        else:
            WarningText("You can not afford this").display()
            return False

    def level_up_prompt(self, entity):
        while True:
            money = get_int(f"lvl {entity.experience.display_level()}\n"
                            f"xp {entity.experience.display_xp()}/{entity.experience.get_xp_required(entity.star_rating.value)}xp\n"
                            f"${self.money}/${entity.get_money_required()}\n"
                            "$1 = 10xp\n"
                            "0 to go back")

            if money == 0:
                break

            if self.can_afford(money):
                self.money -= money
                entity.add_xp(money * 10)

    def exchange_artifact(self, artifact, remove: bool = True):
        star_rating = artifact.star_rating.value
        level = artifact.experience.level
        if remove:
            self.artifact_list.content.remove(artifact)
        return int((level * star_rating) * 100)

    def manage_artifact(self, artifact: Artifact, is_equipped=False):
        while True:
            if artifact is None:
                artifact = self.swap_artifact(artifact)
                return artifact
            elif artifact == "":
                break

            Text(artifact).display()
            choice = get_int(f"1. switch artifact{'' if is_equipped else '(Not equipped)'}\n"
                             f"2. remove artifact{'' if is_equipped else '(Not equipped)'}\n"
                             "3. upgrade artifact\n"
                             "4. back")

            if choice == 1:
                if is_equipped:
                    artifact = self.swap_artifact(artifact)
            elif choice == 2:
                if is_equipped:
                    self.artifact_list.add(artifact)
                    return None
            elif choice == 3:
                if artifact.experience.level != artifact.experience.limit:
                    while True:
                        self.artifact_list.list_content()
                        InfoText("\n\nartifact after level up:\n\n").display()
                        artifact_copy = deepcopy(artifact)
                        artifact_copy.display_info = False

                        for item in self.artifact_list.get_selections():
                            artifact_copy.add_xp(self.exchange_artifact(item, False))

                        Text(artifact_copy).display()
                        inp = self.artifact_list.select(False, list_content=False)
                        if inp is None:
                            break

                        elif isinstance(inp, list):
                            print(inp)
                            for selection in inp:
                                print(self.artifact_list.get(selection))
                                artifact.add_xp(self.exchange_artifact(self.artifact_list.get(selection)))

                            break

                    if not is_equipped:
                        self.artifact_list.add(artifact)  # adds the artifact back

                else:
                    WarningText("Artifact is max level!").display()
            else:
                break

        return artifact

    def manage_weapon(self, weapon):
        while True:
            if weapon is None:
                break
            Text(weapon).display()
            choice = get_int("1. level up\n"
                             "2. back\n")

            if choice == 1:
                self.level_up_prompt(weapon)

            else:
                break

    def manage_character(self, character):
        while True:
            if character is None:
                break
            character.update_stats()
            choice = character.get_option()
            if choice == 1:
                self.level_up_prompt(character)

            elif choice == 2:
                if character.weapon is None:
                    self.swap_weapon(character)

                while character.weapon is not None:
                    Text(character.weapon).display()
                    choice = get_int("1. level up\n"
                                     "2. swap weapon\n"
                                     "3. remove weapon\n"
                                     "4. back\n")

                    if choice == 1:
                        self.level_up_prompt(character.weapon)

                    elif choice == 2:
                        self.swap_weapon(character)
                        character.update_stats()

                    elif choice == 3:
                        self.weapon_list.weapons.append(character.weapon)
                        character.weapon = None

                    else:
                        break

            elif choice == 3:
                for artifact_index in range(5):
                    artifact = character.artifacts.get(artifact_index)
                    Text(f"{artifact_index + 1}. {artifact.list_view() if artifact is not None else 'empty'}").display()
                choice2 = get_int("6. back")
                if choice2 < 6:
                    character.artifacts.set(choice2 - 1,
                                            self.manage_artifact(character.artifacts.get(choice2 - 1), True), True)
                    character.update_stats()

            elif choice == 4:
                return character

            else:
                break

    def swap_artifact(self, artifact_to_swap):
        artifact = self.artifact_list.select()

        if artifact_to_swap is not None:
            self.artifact_list.add(artifact_to_swap)

        return artifact

    def swap_weapon(self, character):
        character_weapon = character.weapon
        character.weapon = self.weapon_list.select()

        if character_weapon is not None:
            self.weapon_list.add(character_weapon)

        Text(f"You have equipped {character.weapon.name}").display()

    def jsonify(self):
        return {
            "artifacts": self.jsonify(),
            "weapons": self.jsonify(),
            "characters": self.jsonify(),
            "money": self.money
        }

    def __repr__(self):
        return (
            f"""
${self.money}
1. characters {self.character_list.get_length()}
2. weapons {self.weapon_list.get_length()}
3. artifacts {self.artifact_list.get_length()}
4. back
"""
        )
