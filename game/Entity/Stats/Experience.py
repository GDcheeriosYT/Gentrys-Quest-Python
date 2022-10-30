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

    def display_level(self):
        return f"level {self.level}{f'/{self.limit}'}" if self.limit is not None else f"level {self.level}"

    def display_xp(self):
        return f"{self.xp}xp"

    def __repr__(self):
        return f"{self.display_level()} {self.display_xp()}"

    # Gives you the amount of xp required to level up given the star rating
    def get_xp_required(self, star_rating, is_artifact=False):
        if is_artifact:
            return int((self.level * 50) * star_rating)
        else:
            return int(((self.level * 75) + ((star_rating * (self.level * 0.25)) * 25)) * ((self.level / 20) + 1))
