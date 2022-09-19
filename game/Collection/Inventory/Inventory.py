class Inventory:
    """
    Holds all the users owned items

    returns an Inventory

    parameters

    inventory_data: json object
        data used to construct inventory
    """

    inventory_data = None
    characters = None
    artifacts = None
    weapons = None
    money = None

    def __init__(self, inventory_data):
        money = 0
