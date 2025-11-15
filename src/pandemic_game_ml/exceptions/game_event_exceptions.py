class GameEventException(Exception):
    pass

class OutbreakException(GameEventException):    
    def __init__(self, city: str, color: str):
        self.city = city
        self.color = color
        super().__init__(f"Outbreak in {city} with {color} disease")

class EpidemicException(GameEventException):
    def __init__(self, qty: int):
        self.qty = qty
        super().__init__(f"Epidemic occurred: {qty} epidemic cards were drawn")