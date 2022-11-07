# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating

# config packages
from Config.StringSetting import StringSetting
from Config.NumberSetting import NumberSetting
from Config.ClassSetting import ClassSetting
from Config.ToggleSetting import ToggleSetting
from Config.SettingManager import SettingManager

# IO packages
from IO.Input import get_int
from IO import Window

# graphics packages
from Graphics.Text.Text import Text


class BattleAreaTestInterface:
    def __init__(self):
        self.character = Character(
            "joe mama",
            "just joe mama",
            StarRating(1)
        )
        self.battle_area = BattleArea("test battle area")
        self.battle_area.artifact_families.add("Brayden Messerschmidt")
        self.battle_area.enemies.add(Enemy())
        self.settings = [
            StringSetting("name", self.battle_area.name),
            NumberSetting("difficulty", self.battle_area.difficulty.value, 0),
            ToggleSetting("can run", self.battle_area.is_runnable),
            ToggleSetting("difficulty scales", self.battle_area.difficulty_scales),
            ClassSetting("artifact families", self.battle_area.artifact_families),
            ClassSetting("enemies", self.battle_area.enemies),
            ClassSetting("character", self.character)
        ]

    def __repr__(self):
        choice = get_int("1. test battle area\n"
                         "2. modify battle area\n"
                         "3. back")

        if choice == 1:
            self.battle_area.start(self.character)

        elif choice == 2:
            while True:
                try:
                    Window.clear()
                    Text(self.battle_area).display()
                    self.settings = SettingManager(self.settings).config_settings()
                    self.name = self.settings[0].text
                    self.battle_area.difficulty.value = self.settings[1].value
                    self.battle_area.is_runnable = self.settings[2].toggled
                    self.battle_area.difficulty_scales = self.settings[3].toggled
                    self.battle_area.artifact_families = self.settings[4].instance_class
                    self.battle_area.enemies = self.settings[5].instance_class
                    self.character = self.settings[6].instance_class
                except TypeError:
                    Window.clear()
                    break

        else:
            raise TypeError
