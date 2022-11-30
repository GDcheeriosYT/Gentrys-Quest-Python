# game packages
# entity packages
from Entity.Stats.Effect.Effect import Effect
from Entity.Stats.Effect.EffectDetails import EffectDetails
from Entity.Stats.Effect.EffectVariables import EffectVariables
from Entity.Stats.StatCollection import StatCollection
from Entity.Stats.StatTypes import StatTypes
from Entity.Stats.StatValueTypes import StatValueTypes

# collection packages
from Collection.ItemList import ItemList

# graphics packages
from Graphics.TextAnimation.TextAnimation import TextAnimation


class Burn(Effect):
    def __init__(self):
        stat_collection = ItemList(content=[
            StatCollection(StatTypes.Attack, StatValueTypes.Flat, -5)
        ])
        variables = EffectVariables(
            False,
            5,
            10,
            stat_collection
        )
        super().__init__(
            EffectDetails(
                "Burn",
                TextAnimation(),
                f"Every {variables.round_cooldown} rounds burns {variables.get_target_string()} for {variables.stat_collection.get(0).amount} damage for {variables.lasts} rounds"
            ),
            variables
        )
