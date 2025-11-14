from exceptions.game_end_exceptions import TooManyOutbreaksException

MAX_OUTBREAKS = 7

class OutbreakCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        if self.count > MAX_OUTBREAKS:
            raise TooManyOutbreaksException(self.count)