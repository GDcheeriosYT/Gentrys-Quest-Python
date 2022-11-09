# game packages
# entity packages
from Entity.Enemy.Enemy import Enemy

# graphic packages
from Graphics.Text.Text import Text

class TestInterfaceEnemy:
    def __init__(self):
        self.enemy = Enemy("Test Enemy")

    def __repr__(self):
        self.enemy = self.enemy.test()