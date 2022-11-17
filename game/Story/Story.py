# game packages
# IO packages
from IO.Input import enter_to_continue

# graphics packages
from Graphics.Text.Text import Text

# location packages
from Location.BattleArea.BattleArea import BattleArea


class Story:
    def __init__(self, events: list):
        self.events = events

    def start(self, character, inventory):
        for event in self.events:
            if isinstance(event, str):
                Text(event.replace("{player}", character.name)).display()

            elif isinstance(event, BattleArea):
                event.start(character, inventory)

            enter_to_continue()
