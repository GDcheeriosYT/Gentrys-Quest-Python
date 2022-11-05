# game packages
# location packages
from ..Area.Area import Area
from .Difficulty import Difficulty

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Entity import Entity
from Entity.Enemy.Enemy import Enemy

# built-in packages
import random


class BattleArea(Area):
    """
    Makes a battle area.
    """

    name = None
    difficulty = None

    def __init__(self, name=Text("battle area"), difficulty=Difficulty(1), artifact_families=ItemList(content_type=str), enemies=ItemList(content_type=Enemy)):
        super().__init__(name)
        self.name.style.text_color = "red"
        self.difficulty = difficulty
        self.artifact_families = artifact_families
        self.enemies = enemies

    def initialize_enemies(self, difficulty):
        enemies = []
        for i in range((difficulty + self.difficulty) * random.randint(1, 3)):
            enemies.append(random.choice(self.enemies.content))

        return enemies

    def start(self, character):
        Text(f"You enter {self.name}!").display()
        enemies = self.initialize_enemies(character.difficulty)
        for enemy in enemies:
            Text(f"You encountered a {enemy}").display()
            Text(enemy).display()
            while (enemy.health > 0) or (character.health > 0):
                Text(f"{enemy.name} {enemy.health}\n"
                     f"{character.name} {character.health}\n").display()

        Text(f"").display()

    def __repr__(self):
        return f"{self.name} {self.difficulty}"
