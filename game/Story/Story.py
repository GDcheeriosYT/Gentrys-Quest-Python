# game packages
# IO packages
from IO.Input import enter_to_continue

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# location packages
from Location.BattleArea.BattleArea import BattleArea

# entity packages
from Entity.Artifact.Artifact import Artifact

# gacha packages
from Gacha.GachaEvent import GachaEvent


class Story:
    def __init__(self, events: list):
        self.events = events

    def start(self, character, inventory, content):
        for event in self.events:
            if isinstance(event, str):
                Text(event.replace("{player}", character.name)).display()
                enter_to_continue()

            elif isinstance(event, BattleArea):
                event.start(character, inventory, content)

            elif isinstance(event, Artifact):
                inventory.artifact_list.add(event)
                Text(f"You have recieved {event}\n"
                     f"Go to {Text('manage artifacts', Style(text_style=['bold'])).raw_output()} to equip it").display()
                enter_to_continue()
                inventory.manage_character(character)

            elif isinstance(event, GachaEvent):
                event.pull(inventory)
