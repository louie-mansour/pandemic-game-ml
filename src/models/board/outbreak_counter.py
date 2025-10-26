MAX_OUTBREAKS = 8

class OutbreakCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        if self.count >= MAX_OUTBREAKS:
            raise Exception("Maximum number of outbreaks reached.")
        self.count += 1