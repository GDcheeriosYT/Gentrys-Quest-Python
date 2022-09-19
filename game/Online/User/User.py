class User:
    """
    makes a user object

    parameters
    username: string
        the username of the user

    powerlevel: PowerLevel
        the powerlevel of the user

    aura: Aura
        the aura of the user
    """

    username = None
    powerlevel = None
    aura = None

    def __init__(self, username, powerlevel=0, aura=None):
        self.username = username
        self.powerlevel = powerlevel
        self.aura = None
