from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience
from Entity.Weapon.Weapon import Weapon
from Entity.Artifact.Artifact import Artifact

from Graphics.Text.Text import Text

from Random.Functions import get_random_name

from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

from Collection.ItemList import ItemList

from IO import Window

class TestCharacterInterface:

    character = None
    settings = None

    def __init__(self):
        name = get_random_name()
        self.character = Character(name)
        self.settings = [
            StringSetting("name", self.character.name),
            NumberSetting("health points", 0, 0),
            NumberSetting("attack points", 0, 0),
            NumberSetting("defense points", 0, 0),
            NumberSetting("critRate points", 0, 0),
            NumberSetting("critDamage points", 0, 0),
            NumberSetting("star rating", self.character.star_rating.value, 1, 5),
            NumberSetting("level", self.character.experience.level, 1),
            ClassSetting("weapon", self.character.weapon),
            ClassSetting("artifacts", self.character.artifacts),
            StringSetting("description", self.character.description)
        ]

    def __repr__(self):
        Window.clear()
        Text(self.character).display()
        self.settings = SettingManager(self.settings).config_settings(False)
        self.character.name = self.settings[0].text
        self.character.default_health_points = self.settings[1].value
        self.character.default_attack_points = self.settings[2].value
        self.character.default_defense_points = self.settings[3].value
        self.character.default_crit_rate_points = self.settings[4].value
        self.character.default_crit_damage_points = self.settings[5].value
        self.character.star_rating = StarRating(self.settings[6].value)
        self.character.experience.level = self.settings[7].value
        self.character.weapon = self.settings[8].instance_class
        self.character.artifacts = self.settings[9].instance_class
        self.character.description = self.settings[10].text
        self.character.update_stats()
        return self.settings
