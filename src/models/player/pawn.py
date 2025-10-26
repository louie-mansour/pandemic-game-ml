from src.models.shared.city import City


class Pawn:
    city: City

    def __init__(self, city: City):
        self.city = city