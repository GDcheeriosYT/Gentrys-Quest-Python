# game packages
# graphics packages
from Graphics.Text.Text import Text

class Area:
    """
    makes an area
    """

    name = None

    def __init__(self, name=Text("Area")):
        self.name = name

    def __repr__(self):
        return Text(f"{self.name}").display()
