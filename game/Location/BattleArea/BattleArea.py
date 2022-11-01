# game packages
# location packages
from ..Area.Area import Area
from .Difficulty import Difficulty

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style


class BattleArea(Area):
    """
    Makes a battle area.
    """

    name = None
    difficulty = None

    def __init__(self, name=Text("battle area"), difficulty=Difficulty(1)):
        super().__init__(name)
        self.name.style.text_color = "red"
        self.difficulty = diff1iculty

    def __repr__(self):
        return f"{self.name} {self.difficulty}"
