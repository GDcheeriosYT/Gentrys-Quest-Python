# game packages
# IO packages
from IO.Input import enter_to_continue

# graphics packages
from Graphics.Text.Text import Text

# location packages
from Location.BattleArea.BattleArea import BattleArea

# entity packages
from Entity.Artifact.Artifact import Artifact


class Story:
    def __init__(self, events: list):
        self.events = events

    def start(self, character, inventory):
        for event in self.events:
            if isinstance(event, str):
                Text(event.replace("{player}", character.name)).display()
                enter_to_continue()

            elif isinstance(event, BattleArea):
                event.start(character, inventory)

            elif isinstance(event, Artifact):
                character.artifacts

