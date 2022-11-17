# game packages
# collection packages
from Collection.ItemList import ItemList

# location packages
from Location.Location import Location

# content packages
from Content.Locations.Iowa.Iowa import Iowa

# IO packages
from IO.Input import get_int
from IO import Window

# interface packages
from Interface.Interfaces.Settings import SettingsInterface

# graphics packages
from Graphics.Content.Text.InfoText import InfoText
from Graphics.Content.Text.WarningText import WarningText


class Game:
    def __init__(self, game_data):
        self.game_data = game_data
        self.equipped_character = None
        self.locations = ItemList(content_type=Location)

    def start(self):
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
                            InfoText("Coming Soon...").display(enter_prompt=True)
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
