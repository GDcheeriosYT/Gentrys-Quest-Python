# game packages
# collection packages
from .ArtifactList import ArtifactList
from .CharacterList import CharacterList
from .WeaponList import WeaponList

# graphics packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Text.Text import Text

# IO packages
from IO.Input import get_int


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
        self.character_list = CharacterList(inventory_data["characters"])
        self.weapon_list = WeaponList(inventory_data["weapons"])
        self.artifact_list = ArtifactList(inventory_data["artifacts"])

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
                    if is_not_empty(self.character_list.characters, "character"):
                        equipped_character = self.manage_character(self.character_list.list_characters())
                elif num == 2:
                    if is_not_empty(self.weapon_list.weapons, "weapon"):
                        self.manage_weapon(self.weapon_list.list_weapons())
                elif num == 3:
                    if is_not_empty(self.artifact_list.artifacts, "artifact"):
                        self.manage_artifact(self.artifact_list.list_artifacts())
                else:
                    break
            except ValueError:
                WarningText("That's not exactly a number... Bro")
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

    def exchange_artifact(self, artifact):
        star_rating = artifact.star_rating.value
        level = artifact.experience.level
        self.artifact_list.artifacts.remove(artifact)
        return int((level * star_rating) * 100)

    def manage_artifact(self, artifact, is_equipped=False):
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
                    self.artifact_list.artifacts.append(artifact)
                    return None
            elif choice == 3:
                if artifact.experience.level != artifact.experience.limit:
                    if not is_equipped:
                        artifact_index = self.artifact_list.artifacts.index(artifact)
                        self.artifact_list.artifacts.remove(artifact)  # removes the artifact from the list so it can't be exchanged by itself
                    for artifact_listing in self.artifact_list.artifacts:
                        Text(
                            f"{self.artifact_list.artifacts.index(artifact_listing) + 1}. {artifact_listing.list_view()}").display()
                    Text(f"{len(self.artifact_list.artifacts) + 1}. back").display()

                    index = get_int("which artifact will you exchange?") - 1
                    if 0 <= index < len(self.artifact_list.artifacts):
                        artifact.add_xp(self.exchange_artifact(self.artifact_list.artifacts[index]))
                    if not is_equipped:
                        self.artifact_list.artifacts.insert(artifact_index, artifact)  # adds the artifact back
                else:
                    WarningText("Artifact is max level!").display()
            else:
                break

        return artifact

    def manage_weapon(self, weapon):
        while True:
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
        for artifact in self.artifact_list.artifacts:
            Text(f"{self.artifact_list.artifacts.index(artifact) + 1}. {artifact.list_view()}").display()
        Text(f"{len(self.artifact_list.artifacts) + 1}. back").display()

        index = get_int("which artifact will you swap?") - 1
        artifact = self.artifact_list.artifacts[index]
        if artifact_to_swap is not None:
            self.artifact_list.artifacts[index] = artifact_to_swap
        else:
            self.artifact_list.artifacts.pop(index)
        return artifact

    def swap_weapon(self, character):
        for weapon in self.weapon_list.weapons:
            Text(f"{self.weapon_list.weapons.index(weapon) + 1}. {weapon.list_view()}").display()
        try:
            character_weapon = character.weapon
            index = get_int(
                f"{'which weapon will you equip?' if character_weapon is None else 'which weapon will you swap?'}\n{len(self.weapon_list.weapons) + 1}. back") - 1
            character.weapon = self.weapon_list.weapons[index]
            if character_weapon is not None:
                self.weapon_list.weapons[index] = character_weapon
            else:
                self.weapon_list.weapons.pop(index)
                Text(f"You have equipped {character.weapon.name}").display()

        except IndexError:
            WarningText("Not in the list")

    def jsonify(self):
        return {
            "artifacts": self.artifact_list.give_artifact_json_list(),
            "weapons": self.weapon_list.give_weapon_json_list(),
            "characters": self.character_list.give_character_json_list(),
            "money": self.money
        }

    def __repr__(self):
        return (
            f"""
${self.money}
1. characters {len(self.character_list.characters)}
2. weapons {len(self.weapon_list.weapons)}
3. artifacts {len(self.artifact_list.artifacts)}
4. back
"""
        )
