# game packages
# location packages
from ..Area.Area import Area
from .Difficulty import Difficulty

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style
from Graphics.Content.Text.WarningText import WarningText

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Entity import Entity
from Entity.Enemy.Enemy import Enemy
from Entity.Artifact.Artifact import Artifact

# IO packages
from IO.Input import get_int, enter_to_continue
from IO import Window

# built-in packages
import random
from copy import copy


class EndException(Exception):
    pass


class BattleArea(Area):
    """
    Makes a battle area.
    """

    name = None
    difficulty = None

    def __init__(self, name, difficulty=0, artifact_families=ItemList(content_type=str),
                 enemies=ItemList(content_type=Enemy), is_runnable=True):
        super().__init__(name)
        self.name = Text(name, Style(text_color="red")).raw_output()
        self.difficulty = Difficulty(difficulty)
        self.artifact_families = artifact_families
        self.enemies = enemies
        self.is_runnable = is_runnable

    def initialize_enemies(self, difficulty):
        enemies = []
        for i in range((difficulty + self.difficulty.value) * random.randint(1, 3)):
            enemies.append(copy(random.choice(self.enemies.content)))

        return enemies

    def initialize_artifacts(self, difficulty):
        artifacts = []
        artifacts_to_choose_from = []
        for family in self.artifact_families.content:
            pass

        for i in range((difficulty + self.difficulty.value) * random.randint(1, 2)):
            pass

        return artifacts

    @staticmethod
    def results(percentage, money=0, xp=0, artifacts=None):
        Window.place_rule("Battle Area Results")
        Text(f"completion {percentage}%\n"
             "You received:\n"
             f"${money}\n"
             f"{xp}xp\n"
             f"{artifacts}").display()
        enter_to_continue()
        raise EndException

    def start(self, character):
        try:
            Text(f"You enter {self.name}!").display()
            enemies = self.initialize_enemies(character.difficulty)
            enemies_killed = 0
            money = 0
            xp = 0
            percentage = 0

            def calculate_percentage():
                nonlocal percentage
                percentage = int((enemies_killed / len(enemies)) * 100)

            for enemy in enemies:
                calculate_percentage()
                Text(f"You encountered an {enemy}").display()
                enemy.show_stats()
                while True:
                    Text(f"{enemy.name} {enemy.health}\n"
                         f"{character.name} {character.health}\n").display()
                    options = character.get_battle_options()
                    if self.is_runnable:
                        options.append("run")

                    for option in options:
                        print(f"{options.index(option) + 1}. {option}")

                    if character.manage_battle_input(get_int(""), enemy, options):
                        if enemy.health <= 0:
                            Text(f"{enemy.name} is dead\n"
                                 f"you received ${enemy.get_money()} and {enemy.get_xp()}xp").display()
                            xp += enemy.get_xp()
                            money += enemy.get_money()
                            character.add_xp(enemy.get_xp())
                            enter_to_continue()
                            break
                        else:
                            enemy.attack_character(character)
                            if character.health <= 0:
                                WarningText(f"{character.name} has died").display()
                                enter_to_continue()
                                self.results(percentage, money, xp)
                    else:
                        self.results(percentage, money, xp)

                enemies_killed += 1
                calculate_percentage()
            self.results(percentage, money, xp)
        except EndException:
            pass

    def __repr__(self):
        return f"{self.name} {self.difficulty.__repr__()}"
