# game packages
# story packages
from Story.Story import Story

# collection packages
from Collection.ItemList import ItemList

# location packages
from Location.BattleArea.BattleArea import BattleArea

# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.Buff import Buff

# built-in packages
import random


class Intro(Story):
    def __init__(self):
        artifacts = ItemList(content_type=str)
        artifacts.content = [""]
        enemies = ItemList(content_type=Enemy)
        angry_pedestrian = Enemy(
            "Angry Pedestrian",
            0,
            10,
            0,
            Weapon(
                "Knife",
                "Slices things...",
                "Knife",
                0,
                Buff(),
                Verbs("Sliced", "Stabbed")
            ),
            "A very angry pedestrian."
        )
        enemies.add(angry_pedestrian)
        intro_fight = BattleArea(
            "The Streets",
            0,
            artifacts,
            enemies,
            False,
            False
        )
        super().__init__(
            [
                "It's 10PM.",
                "{player} is out buying instant noodles.",
                f"They purchase {random.randint(2, 7)} noodles and leave.",
                f"As they are walking home, an angry pedestrian runs up to them and commands they give them ${random.randint(100, 300)}.",
                "{player} refuses.",
                "\"You leave me no choice...\" says the angry pedestrian.",
                "{player} prepares for battle",
                intro_fight,
                "{player} wakes up."
            ]
        )
