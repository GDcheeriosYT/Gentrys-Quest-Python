# game packages
# entity packages
from Entity.Stats.Effect.Effect import Effect
from Entity.Stats.Effect.EffectDetails import EffectDetails



# collection packages
from Collection.ItemList import ItemList


class Burning(Effect):
    def __init__(self):
        super().__init__(
            EffectDetails(
                "Burning",
                None,
                "[orange]Burns[white], idk..."
            )
        )