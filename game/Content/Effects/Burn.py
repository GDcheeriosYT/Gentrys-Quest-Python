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
from Graphics.Text.Text import Text


class Burn(Effect):
    def __init__(self):
        stat_collection = ItemList(content=[
            StatCollection(StatTypes.Attack, StatValueTypes.Flat, 5)
        ])
        variables = EffectVariables(
            False,
            2,
            3,
            stat_collection
        )
        super().__init__(
            EffectDetails(
                "Burn",
                TextAnimation(),
                f"Every {variables.round_cooldown} turns burns {variables.get_target_string()} for {variables.stat_collection.get(0).amount} damage for {variables.lasts} turns"
            ),
            variables
        )

    def level_up(self):
        self.experience.level += 1
        self.variables.round_cooldown = int(3 - ((self.experience.level / 2) if (self.experience.level / 2) < 3 else 0))
        self.variables.lasts = int(2 + self.experience.level / 2)
        self.variables.stat_collection.get(0).amount = int(5 + (self.experience.level * 3.5))
        self.details.description = Text(f"Every {self.variables.round_cooldown} turns burns {self.variables.get_target_string()} for {self.variables.stat_collection.get(0).amount} damage for {self.variables.lasts} turns")
