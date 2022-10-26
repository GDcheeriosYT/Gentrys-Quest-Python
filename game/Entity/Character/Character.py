# game packages
# entity packages
from ..Entity import Entity
from ..Weapon.Weapon import Weapon
from ..Stats.StatTypes import StatTypes
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
    health = None
    attack = None
    defense = None
    critRate = None
    critDamage = None
    default_health = None
    default_attack = None
    default_defense = None
    default_crit_rate = None
    default_crit_damage = None
    additional_health = None
    additional_attack = None
    additional_defense = None
    additional_critRate = None
    additional_critDamage = None
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
        self.get_buff_values()
        self.health = self.default_health + self.additional_health
        self.attack = self.default_attack + self.additional_attack
        self.defense = self.default_defense + self.additional_defense
        self.critRate = self.default_crit_rate + self.additional_critRate
        self.critDamage = self.default_crit_damage + self.additional_critDamage

    def get_buff_values(self):
        buffs = self.create_buff_groups()
        health = 0
        attack = 0
        defense = 0
        critRate = 0
        critDamage = 0

        def determine_value(default_stat, buff):
            if buff.is_percent:
                return int(default_stat * (buff.value * 0.01))
            else:
                return buff.value

        for buff in buffs["health"]:
            health += determine_value(self.default_health, buff)

        for buff in buffs["attack"]:
            attack += determine_value(self.default_attack, buff)

        for buff in buffs["defense"]:
            defense += determine_value(self.default_defense, buff)

        for buff in buffs["critRate"]:
            critRate += determine_value(self.default_crit_rate, buff)

        for buff in buffs["critDamage"]:
            critDamage += determine_value(self.default_crit_damage, buff)

        self.additional_health = health
        self.additional_attack = attack
        self.additional_defense = defense
        self.additional_critRate = critRate
        self.additional_critDamage = critDamage

    def create_buff_groups(self):
        health = []
        attack = []
        defense = []
        critRate = []
        critDamage = []
        def check_buff(buff):
            if buff.attribute_type == StatTypes.Health:
                health.append(buff)
            elif buff.attribute_type == StatTypes.Attack:
                attack.append(buff)
            elif buff.attribute_type == StatTypes.Defense:
                defense.append(buff)
            elif buff.attribute_type == StatTypes.CritRate:
                critRate.append(buff)
            elif buff.attribute_type == StatTypes.CritDamage:
                critDamage.append(buff)

        if self.weapon is not None:
            check_buff(self.weapon.buff)

        for artifact in self.artifacts.content:
            if artifact is not None:
                check_buff(artifact.main_attribute)
                for attribute in artifact.attributes:
                    check_buff(attribute)

        return {
            "health": health,
            "attack": attack,
            "defense": defense,
            "critRate": critRate,
            "critDamage": critDamage,
        }

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
xp: {self.experience.xp} / {self.experience.get_xp_required(self.star_rating.value)}xp {round(self.experience.xp / self.experience.get_xp_required(self.star_rating.value), 2)}% 
health: {self.default_health} {f"+ {self.additional_health} ({self.health})" if self.additional_health > 0 else ""}
attack: {self.default_attack} {f"+ {self.additional_attack} ({self.attack})" if self.additional_attack > 0 else ""}
defense: {self.default_defense} {f"+ {self.additional_defense} ({self.defense})" if self.additional_defense > 0 else ""}
crit rate: {self.default_crit_rate}% {f"+ {self.additional_critRate}% ({'100%' if self.critRate > 100 else self.critRate})" if self.additional_critRate > 0 else ""}
crit damage: {self.default_crit_damage} {f"+ {self.additional_critDamage} ({self.critDamage})" if self.additional_critDamage > 0 else ""}
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
