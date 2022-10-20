class Experience:
    """
    experience for an Entity object

    parameters

    xp, level: int
        values for experience
    """

    xp = None
    xp_required = None
    level = None

    def __init__(self, level=1, xp=0, limit=None):
        self.level = level
        self.xp = xp
        self.limit = limit

    def __repr__(self):
        return f"level {self.level}{f'/{self.limit}' if self.limit is not None else ''} {self.xp}xp"

    # Gives you the amount of xp required to level up given the star rating
    def get_xp_required(self, star_rating):
        return int(((self.level * 100) + (star_rating * 1.25)) * ((self.level / 20) + 1))
