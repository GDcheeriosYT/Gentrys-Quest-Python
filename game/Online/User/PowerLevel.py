class PowerLevel:
    """
    makes a power level for a user object

    parameters
    rankings: tuple
        tuple of points for each criteria.
    """

    powerlevel = None
    rankings = None

    def __init__(self, rankings=(0, 0)):
        self.powerlevel = rankings[0] + rankings[1]