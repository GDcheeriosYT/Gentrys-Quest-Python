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
from Entity.Enemy.Enemy import Enemy
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating

# IO packages
from IO.Input import get_int, enter_to_continue
from IO import Window

# content packages
from Content.ArtifactContentManager import ArtifactContentManager

# random packages
from Random.Functions import generate_artifact_star_rating

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

    @staticmethod
    def apply_random_level(number):
        def get_min(number, difference):
            while number - difference <= 0:
                print("poop1: ", number - difference, end="\r")
                difference -= 1

            return difference

        def get_max(number, difference):
            print("poop2: ", number - difference, end="\r")
            while number + difference >= 20:
                difference -= 1

            return difference

        number_diff = 3
        min = get_min(number, number_diff)
        max = get_max(number, number_diff)
        if min < max:
            number_diff = min
        else:
            number_diff = max
        return number + random.randint(-abs(number_diff), number_diff)

    def initialize_enemies(self, character):
        enemies = []
        difficulty = self.get_difficulty(character.difficulty)
        for i in range((difficulty + random.randint(0, difficulty))):
            enemy = copy(random.choice(self.enemies.content))
            level = self.apply_random_level(character.experience.level % 20)
            enemy.experience.level = (20 * (self.get_difficulty(character.difficulty) - 1)) + level
            enemy.update_stats()
            enemies.append(enemy)

        return enemies

    def initialize_artifacts(self, difficulty):
        points = self.get_difficulty(difficulty) * 100
        families = ArtifactContentManager().load_content()
        artifacts = []
        artifacts_to_choose_from = []
        for family in self.artifact_families.content:
            for family1 in families:
                if family == family1.name:
                    for artifact in family1.artifacts:
                        artifacts_to_choose_from.append(artifact)

        while points > 0:
            artifact = random.choice(artifacts_to_choose_from)
            star_rating = generate_artifact_star_rating(self.get_difficulty(difficulty))
            artifact = artifact(StarRating(star_rating))
            artifacts.append(artifact)
            if star_rating == 1:
                points -= 25

            elif star_rating == 2:
                points -= 45

            elif star_rating == 3:
                points -= 65

            elif star_rating == 4:
                points -= 75

            else:
                points -= 100

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
            if character is None:
                WarningText("You do not have a character equipped!").display()
                raise EndException
            character.update_stats()
            Text(f"You enter {self.name}!").display()
            enemies = ItemList(content_type=Enemy)
            enemies.content = self.initialize_enemies(character)
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
                Text(f"{character.name} encountered a {enemy}").display()
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
            if character is not None:
                character.update_stats()
            pass

    def __repr__(self):
        return f"{self.name} {self.difficulty.__repr__()}"
