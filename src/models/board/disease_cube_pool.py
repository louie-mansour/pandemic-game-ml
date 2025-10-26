from src.models.shared.colour import Colour


class DiseaseCubePool:
    RED_CUBES = 24
    BLUE_CUBES = 24
    YELLOW_CUBES = 24
    BLACK_CUBES = 24

    def __init__(self):
        self.red_cubes = self.RED_CUBES
        self.blue_cubes = self.BLUE_CUBES
        self.yellow_cubes = self.YELLOW_CUBES
        self.black_cubes = self.BLACK_CUBES

    def remove_cubes(self, color: Colour, qty: int) -> None:
        if color == Colour.RED:
            if qty > self.red_cubes:
                raise Exception("Not enough red cubes in the pool.")
            self.red_cubes -= qty
        elif color == Colour.BLUE:
            if qty > self.blue_cubes:
                raise Exception("Not enough blue cubes in the pool.")
            self.blue_cubes -= qty
        elif color == Colour.YELLOW:
            if qty > self.yellow_cubes:
                raise Exception("Not enough yellow cubes in the pool.")
            self.yellow_cubes -= qty
        elif color == Colour.BLACK:
            if qty > self.black_cubes:
                raise Exception("Not enough black cubes in the pool.")
            self.black_cubes -= qty

    def add_cubes(self, color: str, qty: int) -> None:
        if color == "red":
            self.red_cubes += qty
        elif color == "blue":
            self.blue_cubes += qty
        elif color == "yellow":
            self.yellow_cubes += qty
        elif color == "black":
            self.black_cubes += qty