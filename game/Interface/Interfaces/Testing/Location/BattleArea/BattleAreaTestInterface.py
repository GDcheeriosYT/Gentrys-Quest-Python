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

# IO packages
from IO.Input import get_int

class BattleAreaTestInterface:
    def __init__(self):
        self.character = Character(
            "joe mama",
            "just joe mama",
            StarRating(1)
        )
        self.battle_area = BattleArea("test battle area", 0, ItemList(content_type=str), ItemList(content_type=Enemy))
        self.settings = [
            StringSetting("name", self.battle_area.name),
            NumberSetting("difficulty", self.battle_area.difficulty),
            ClassSetting("artifact families", self.battle_area.artifact_families),
            ClassSetting("enemies", self.battle_area.enemies),
            ClassSetting("character", self.character)
        ]

    def test(self):
        choice = get_int("1. test battle area\n"
                         "2. modify battle area\n"
                         "3. back")

        if choice == 1:
            self.battle_area.start(self.character)
