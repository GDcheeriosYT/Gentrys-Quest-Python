# game packages
# entity packages
from ..Entity import Entity
from ..Weapon.Weapon import Weapon
from ..Stats.StarRating import StarRating
from ..Stats.Experience import Experience
from ..Artifact.Artifact import Artifact

# collection packages
from Collection.ItemList import ItemList

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Content.Text.WarningText import WarningText

# IO packages
from IO import Window


class Character(Entity):
    """
    Makes a Character class

    parameters

    name: string
        the name of the Character

    description: string
        the description of the Character

    star_rating: int
        the star rating of the Character

    experience: Experience
        the experience of the Character

    weapon: Weapon
        the Weapon that the Character has equipped

    artifacts: ItemList
        the Artifacts that the character has

    default_health_points: int
        the default health points the Character has

    default_attack_points: int
        the default attack points damage that the Character does

    default_defense_points: int
        the default defense points that the Character has

    default_crit_rate_points: int
        the default crit rate points the Character has

    default_crit_damage_points: int
        the default crit damage points the character has
    """

    name = None
    description = None
    star_rating = None
    experience = None
    weapon = None
    artifacts = None
    default_health_points = None
    default_attack_points = None
    default_defense_points = None
    default_crit_rate_points = None
    default_crit_damage_points = None
    default_health = None
    default_attack = None
    default_defense = None
    default_crit_rate = None
    default_crit_damage = None
    difficulty = None

    def __init__(self, name, description="description", star_rating=StarRating(1), experience=Experience(), weapon=Weapon(),
                 artifacts=ItemList(5, Artifact, True), default_health_points=0, default_attack_points=0,
                 default_defense_points=0, default_crit_rate_points=0,
                 default_crit_damage_points=0):
        super().__init__(name, description, star_rating, experience)
        self.default_health_points = default_health_points
        self.default_attack_points = default_attack_points
        self.default_crit_rate_points = default_crit_rate_points
        self.default_defense_points = default_defense_points
        self.default_crit_damage_points = default_crit_damage_points
        self.weapon = weapon
        self.artifacts = artifacts
        self.update_stats()

    def update_stats(self):
        self.difficulty = int(1 + (self.experience.level / 20))
        self.default_health = int((((((self.star_rating.value - 1) * 3.5) + (((self.experience.level - 1) * 2.5) + ((self.star_rating.value - 1) * (self.experience.level * 0.5)))) * self.check_minimum(self.default_health_points, 1.12)) * self.check_minimum(self.difficulty - 1, 1.60)) + 20)
        self.default_attack = int((self.check_minimum(self.star_rating.value * (self.check_minimum(self.experience.level * 0.32)), 0.80) + (self.check_minimum(self.default_attack_points, 1, True) * (self.experience.level / 4))) * self.check_minimum(self.difficulty - 1, 1.60)) + 2
        self.default_defense = int((self.check_minimum(self.star_rating.value * (self.check_minimum(self.experience.level * 0.32)), 0.5) + (self.check_minimum(self.default_defense_points, 1, True)) * (self.experience.level / 8)) * self.check_minimum(self.difficulty - 1, 1.60)) + 1
        default_crit_rate = float(self.check_minimum(self.default_crit_rate_points, 3) + self.check_minimum(self.star_rating.value, 0.5) + self.check_minimum(self.experience.level, 0.45) + 3)
        self.default_crit_rate = 100 if default_crit_rate >= 100 else default_crit_rate
        self.default_crit_damage = int((self.check_minimum(self.star_rating.value * (self.check_minimum(self.experience.level * 0.28)), 0.15) + (self.check_minimum(self.default_crit_damage_points, 1, True) * (self.experience.level / 2.5))) * self.check_minimum(self.difficulty - 1, 1.60)) + 2

    def level_up(self, amount):
        self.experience.level += amount
        self.update_stats()

    def add_xp(self, amount):
        difference = self.experience.get_xp_required(self.star_rating.value) - self.experience.xp
        still_upgrading = True
        while still_upgrading:
            if self.experience.xp + amount > self.experience.get_xp_required(self.star_rating.value):
                amount -= difference
                self.level_up(1)
                self.experience.xp = difference
                difference = self.experience.get_xp_required(self.star_rating.value) - self.experience.xp
            else:
                self.experience.xp += amount
                still_upgrading = False

    def level_menu(self, data):
        percentage = self.experience.xp / self.experience.get_xp_required(self.star_rating.value, True)
        Text(f"""
{self.experience}
{self.experience.xp}xp/{self.experience.get_xp_required(self.star_rating.value, True)}xp ({percentage})%
upgrade your character?
/{(self.experience.xp/10) if int(str(self.experience.xp)[len(str(self.experience.xp)) - 1]) != 0 else (self.experience.xp/10) + 1}
""")

    def manage(self):
        while True:
            Window.clear()
            Text(self.__repr__()).display()
            try:
                choice = int(input("1. level up\n"
                                   "2. manage weapon\n"
                                   "3. manage artifacts\n"
                                   "4. equip character\n"
                                   "5. back"))
                if choice == 1:
                    pass
                    #not sure what to do yet...

            except ValueError:
                WarningText("That's literally not a number homie...").display()

    def __repr__(self):
        return (
            f"""
{self.name} {self.star_rating}
level {self.experience.level}
xp: {self.experience.xp} / {self.experience.get_xp_required(self.star_rating.value)}xp {self.experience.xp / self.experience.get_xp_required(self.star_rating.value)}% 
health: {self.default_health}
attack: {self.default_attack}
defense: {self.default_defense}
crit rate: {self.default_crit_rate}%
crit damage: {self.default_crit_damage}
--------weapon--------
{self.weapon}
^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(0)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(1)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(2)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(3)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(4)}

====================
{self.description}
====================
"""
        )
