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

    def start_intro(self):
        intro_scene = Intro()
        Window.clear()
        name = get_string("What is this protagonists name?\n")
        character = Character(
            name,
            "The Guy",
            weapon=Weapon(),
            default_attack_points=1,
            default_health_points=1,
            default_defense_points=1,
            default_crit_damage_points=1,
            default_crit_rate_points=1
        )
        self.equipped_character = character
        self.game_data.inventory.character_list.characters.append(character)
        time.sleep(1)
        intro_scene.start(self.equipped_character, self.game_data.inventory)
        character.weapon = self.game_data.inventory.weapon_list.weapons[0]
        self.game_data.inventory.weapon_list.weapons.pop(0)

    def start(self):
        if self.game_data.startup_amount < 1:
            self.start_intro()

        self.game_data.startup_amount += 1
        in_game = True
        while in_game:
            try:
                choices = get_int("Main Menu\n"
                                  "1. Play\n"
                                  "2. Settings\n"
                                  "3. Changelog\n"
                                  "4. Quit")
                if choices == 1:
                    choices1 = get_int("1. Singleplayer\n"
                                       "2. Multiplayer\n"
                                       "3. Back")
                    if choices1 == 1:
                        choices2 = get_int("1. Travel\n"
                                           "2. Gacha\n"
                                           "3. Inventory")

                        if choices2 == 1:
                            iowa = Iowa()
                            choices3 = get_int("1. Iowa\n"
                                               "2. back")

                            if choices3 == 1:
                                iowa.list_areas()
                                iowa.select_area(self.equipped_character, self.game_data.inventory)

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

                    elif choices1 == 2:
                        InfoText("Coming Soon...").display(enter_prompt=True)

                elif choices == 2:
                    Window.clear()
                    self.game_data.settings = SettingsInterface(self.game_data).visit()

                else:
                    in_game = False
            except ValueError:
                WarningText("Number please...").display()
