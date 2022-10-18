# game packages
# entity packages
from ..Entity import Entity
from ..Stats.StarRating import StarRating
from ..Stats.Experience import Experience
from ..Stats.StatTypes import StatTypes
from ..Stats.Buff import Buff

# Config packages
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# Graphics packages
from Graphics.Text.Text import Text

# IO packages
from IO import Window

class Weapon(Entity):
    """
    Makes a weapon

    parameters

    name: string
        the name of the Weapon

    description: string
        the description of the Weapon

    weapon_type: string
        the weapon type

    attack: int
        the attack damage that the Weapon does

    buff: Buff
        the attribute of the user to buff

    verbs: Verbs
        the verbs to be used by the weapon

    star_rating: StarRating
        the star rating of the Weapon

    experience: Experience
        the experience for the Weapon
    """

    name = None
    description = None
    weapon_type = None
    attack = None
    buff = None
    verbs = None
    star_rating = None
    experience = None

    def __init__(self, name="fists", description="punches things", weapon_type=None, attack=3,
                 buff=Buff(StatTypes.Health, Experience(), False), verbs=None, star_rating=StarRating(), experience=Experience()):
        super().__init__(name, description, star_rating, experience)
        self.weapon_type = weapon_type
        self.attack = attack
        self.buff = buff
        self.verbs = verbs
        self.settings = [
            StringSetting("name", self.weapon.name),
            StringSetting("description", self.weapon.description),
            StringSetting("weapon_type", self.weapon.weapon_type),
            NumberSetting("attack", self.weapon.attack),
            ClassSetting("buff", self.weapon.buff),
            ClassSetting("verbs", self.weapon.verbs),
            NumberSetting("star_rating", self.weapon.star_rating.value, 1, 5),
            NumberSetting("experience", self.weapon.experience.level, 1)
        ]

    def __repr__(self):
        return (
f"""
{self.name} {self.star_rating} {self.experience}
"meow " type: {self.weapon_type}
base attack: {self.attack}
attribute: {self.buff}
"""
        )

    def test(self):
        Window.clear()
        Text(self.weapon).display()
        self.settings = SettingManager(self.settings).config_settings(False)
        self.weapon.name = self.settings[0].text
        self.weapon.description = self.settings[1].text
        self.weapon.weapon_type = self.settings[2].text
        self.weapon.attack = self.settings[3].value
        self.weapon.buff = self.settings[4].instance_class
        self.weapon.verbs = self.settings[5].instance_class
        self.weapon.star_rating = StarRating(self.settings[6].value)
        self.weapon.experience.level = self.settings[7].value
        return self.settings
