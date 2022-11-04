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
        self.money = inventory_data["money"]
        self.character_list = CharacterList(inventory_data["characters"])
        self.weapon_list = WeaponList(inventory_data["weapons"])
        self.artifact_list = ArtifactList(inventory_data["artifacts"])

    def upgrade(self):
        pass

    def manage_input(self):
        while True:
            try:
                num = get_int(self.__repr__())
                if num == 1:
                    character = self.character_list.list_characters()
                    if character is not None:
                        self.manage_character(character)
                elif num == 2:
                    weapon = self.weapon_list.list_weapons()
                    if weapon is not None:
                        self.manage_weapon(weapon)
                elif num == 3:
                    artifact = self.artifact_list.list_artifacts()
                    if artifact is not None:
                        self.manage_artifact(artifact)
                else:
                    break
            except ValueError:
                WarningText("That's not exactly a number... Bro")
            except IndexError:
                break

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
        return int((star_rating * 10) + (star_rating * (level * 25)))

    def manage_artifact(self, artifact):
        while True:
            if artifact is None:
                artifact = self.swap_artifact(artifact)

            Text(artifact).display()
            choice = get_int("1. switch artifact\n"
                             "2. remove artifact\n"
                             "3. upgrade artifact\n"
                             "4. back")

            if choice == 1:
                artifact = self.swap_artifact(artifact)
            elif choice == 2:
                self.artifact_list.artifacts.append(artifact)
                artifact = None
            elif choice == 3:
                if artifact.experience.level != artifact.experience.limit:
                    for artifact_listing in self.artifact_list.artifacts:
                        Text(f"{self.artifact_list.artifacts.index(artifact_listing) + 1}. {artifact_listing.list_view()}").display()

                    index = get_int("which artifact will you exchange?") - 1
                    artifact.add_xp(self.exchange_artifact(self.artifact_list.artifacts[index]))
            else:
                WarningText("Artifact is max level!").display()
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
            choice = character.get_option()
            if choice == 1:
                self.level_up_prompt(character)

            elif choice == 2:
                while True:
                    Text(character.weapon).display()
                    choice = get_int("1. level up\n"
                                     "2. swap weapon\n"
                                     "3. back\n")

                    if choice == 1:
                        self.level_up_prompt(character.weapon)

                    elif choice == 2:
                        self.swap_weapon(character)
                        character.update_stats()
                    else:
                        break

            elif choice == 3:
                for artifact_index in range(5):
                    Text(f"{artifact_index + 1}. {character.artifacts.get(artifact_index)}").display()
                choice2 = get_int("6. back")
                if choice2 < 6:
                    character.artifacts.set(choice2 - 1, self.manage_artifact(character.artifacts.get(choice2 - 1)))
                    character.update_stats()

            else:
                break

    def swap_artifact(self, artifact_to_swap):
        for artifact in self.artifact_list.artifacts:
            Text(f"{self.artifact_list.artifacts.index(artifact) + 1}. {artifact.list_view()}").display()

        index = get_int("which artifact will you swap?") - 1

        artifact = self.artifact_list.artifacts[index]
        self.artifact_list.artifacts[index] = artifact_to_swap if artifact_to_swap is not None else self.artifact_list.artifacts.pop(index)
        return artifact

    def swap_weapon(self, character):
        for weapon in self.weapon_list.weapons:
            Text(f"{self.weapon_list.weapons.index(weapon)}. {weapon.list_view()}").display()
        try:
            character_weapon = character.weapon
            index = get_int("which weapon will you swap?") - 1
            character.weapon = self.weapon_list.weapons[index]
            self.weapon_list.weapons[index] = character_weapon
        except IndexError:
            WarningText("Not in the list")

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