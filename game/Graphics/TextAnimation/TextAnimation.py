# game packages

# external packages

class TextAnimation:
    """
    Makes an animation format for Text object

    parameters

    interval: int, double
        the interval between frames

    text_frames: list
        the list of TextFrames
    """

    interval = None
    text_frames = None

    def __init__(self, interval=0.3, text_frames=[]):
        self.interval = interval
        self.text_frames = text_frames
