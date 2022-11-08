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
from Entity.Stats.StarRating import StarRating

# IO packages
from IO.Input import get_int, enter_to_continue
from IO import Window

# content packages
from Content.ArtifactContentManager import ArtifactContentManager

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
                 enemies=ItemList(content_type=Enemy), is_runnable=True, difficulty_scales=True):
        super().__init__(name)
        self.name = Text(name, Style(text_color="red")).raw_output()
        self.difficulty = Difficulty(difficulty)
        self.artifact_families = artifact_families
        self.enemies = enemies
        self.is_runnable = is_runnable
        self.difficulty_scales = difficulty_scales

    def get_difficulty(self, difficulty):
        if self.difficulty_scales:
            return difficulty + self.difficulty.value
        else:
            return self.difficulty

    def initialize_enemies(self, difficulty):
        enemies = []
        for i in range((self.get_difficulty(difficulty)) * random.randint(1, 3)):
            enemies.append(copy(random.choice(self.enemies.content)))

        return enemies

    def initialize_artifacts(self, difficulty):
        families = ArtifactContentManager().load_content()
        artifacts = []
        artifacts_to_choose_from = []
        for family in self.artifact_families.content:
            for family1 in families:
                if family == family1.name:
                    for artifact in family1.artifacts:
                        artifacts_to_choose_from.append(artifact)

        for i in range((self.get_difficulty(difficulty)) * random.randint(1, 2)):
            artifact = random.choice(artifacts_to_choose_from)
            artifact = artifact(StarRating(1))
            artifacts.append(artifact)


        return artifacts

    @staticmethod
    def results(percentage, money=0, xp=0, artifacts=None):
        Window.place_rule("Battle Area Results")
        Text(f"completion {percentage}%\n"
             "You received:\n"
             f"${money}\n"
             f"{xp}xp\n").display()
        if artifacts is not None:
            print("\tartifacts")
            Text(artifacts.list_content()).display()
        enter_to_continue()
        raise EndException

    def start(self, character, inventory):
        try:
            Text(f"You enter {self.name}!").display()
            enemies = ItemList(content_type=Enemy)
            enemies.content = self.initialize_enemies(character.difficulty)
            artifacts = ItemList(content_type=Artifact)
            artifacts.content = self.initialize_artifacts(character.difficulty)
            enemies_killed = 0
            money = 0
            xp = 0
            percentage = 0

            def calculate_percentage():
                nonlocal percentage
                percentage = int((enemies_killed / len(enemies.content)) * 100)

            for enemy in enemies.content:
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
                            inventory.money += enemy.get_money()
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

            for artifact in artifacts.content:
                inventory.artifact_list.artifacts.append(artifact)

            self.results(percentage, money, xp, artifacts)
        except EndException:
            pass

    def __repr__(self):
        return f"{self.name} {self.difficulty.__repr__()}"
