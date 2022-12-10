# game packages
# collection packages
from Collection.ItemList import ItemList

# location packages
from Location.Location import Location

# content packages
from Content.Locations.Iowa.Iowa import Iowa
from Content.Stories.Intro import Intro
from Content.Gachas.ValleyHighSchool import ValleyHighSchool
from Content.Gachas.BaseGacha import BaseGacha
from Content.CharacterContentManager import CharacterContentManager

# IO packages
from IO.Input import get_int, get_string, enter_to_continue
from IO import Window

# entity packages
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon

# interface packages
from Interface.Interfaces.Settings import SettingsInterface

# graphics packages
from Graphics.Content.Text.InfoText import InfoText
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Text.Text import Text

# built-in packages
import time


class Game:
    def __init__(self, game_data):
        self.game_data = game_data
        self.equipped_character = None
        self.locations = ItemList(content_type=Location)

    def start_intro(self, character_name):
        intro_scene = Intro()
        Window.clear()
        characters = self.game_data.content.characters
        self.equipped_character = None
        if character_name is not None:
            for character in characters:
                try:
                    character = character()
                    if character.name == character_name:
                        Text("Thanks for contributing to Gentry's Quest!\nAs a gift take this:").display()
                        Text(character.list_view()).display()
                        self.equipped_character = character
                        enter_to_continue()
                        break
                except TypeError:
                    pass

            if self.equipped_character is None:
                WarningText("We couldn't find this character...").display()
                exit(1)

        else:
            name = get_string("What is this protagonists name?\n")
            character = Character(
                name,
                "The Guy",
                default_attack_points=1,
                default_health_points=1,
                default_defense_points=1,
                default_crit_damage_points=1,
                default_crit_rate_points=1
            )
            self.equipped_character = character

        self.equipped_character.weapon = Weapon()
        self.game_data.inventory.character_list.characters.append(character)
        time.sleep(1)
        intro_scene.start(self.equipped_character, self.game_data.inventory, self.game_data.content)
        character.weapon = self.game_data.inventory.weapon_list.weapons[0]
        self.game_data.inventory.weapon_list.weapons.pop(0)

    def start(self, character_arg):
        if self.game_data.startup_amount < 1:
            self.start_intro(character_arg)

        self.game_data.startup_amount += 1
        in_game = True
        while in_game:
            try:
                choices = get_int("Main Menu\n"
                                  "1. Play\n"
                                  "2. Settings\n"
                                  "3. Quit")

                if choices == 1:
                    while True:
                        choices1 = get_int("1. Singleplayer\n"
                                           "2. Back")
                        if choices1 == 1:
                            while True:
                                choices2 = get_int("1. Travel\n"
                                                   "2. Gacha\n"
                                                   "3. Inventory\n"
                                                   "4. Back")

                                if choices2 == 1:
                                    while True:
                                        locations = self.game_data.content.locations
                                        for location in locations:
                                            Text(f"{locations.index(location) + 1}. {location}").display()
                                        choices3 = get_int(f"{len(locations) + 1}. back")

                                        if choices3 != len(locations) + 1:
                                            try:
                                                location = locations[choices3 - 1]
                                                location.list_areas()
                                                location.select_area(self.equipped_character, self.game_data.inventory,
                                                                     self.game_data.content)
                                            except IndexError:
                                                pass

                                        else:
                                            break

                                elif choices2 == 2:
                                    valley_high_school = ValleyHighSchool()
                                    base_gacha = BaseGacha()
                                    Text(f"1. {valley_high_school.name.raw_output()}\n"
                                         f"2. {base_gacha.name.raw_output()}").display()
                                    choices3 = get_int("3. back")

                                    if choices3 == 1:
                                        valley_high_school.manage_input(self.game_data.inventory)

                                    elif choices3 == 2:
                                        base_gacha.manage_input(self.game_data.inventory)

                                elif choices2 == 3:
                                    inventory_results = self.game_data.inventory.manage_input(self.equipped_character)
                                    if inventory_results is not None:
                                        self.equipped_character = inventory_results

                                else:
                                    break

                        else:
                            break

                elif choices == 2:
                    Window.clear()
                    try:
                        self.game_data.settings = SettingsInterface(self.game_data).visit()
                    except TypeError:
                        Window.clear()

                elif choices == 3:
                    in_game = False
            except ValueError:
                WarningText("Number please...").display()
