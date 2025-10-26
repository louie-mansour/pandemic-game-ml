class InfectionRate:
    RATES = [2, 2, 2, 3, 3, 4, 4]

    def __init__(self):
        self.index = 0

    @property
    def current_rate(self) -> int:
        return self.RATES[self.index]

    def increase(self):
        if self.index < len(self.RATES) - 1:
            self.index += 1