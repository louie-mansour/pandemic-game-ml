from exceptions.game_end_exceptions import DiseaseCubesDepletedException
from models.shared.colour import Colour


class DiseaseCubePool:
    MAX_CUBES = 24

    def __init__(self):
        self.cubes = {
            Colour.RED: self.MAX_CUBES,
            Colour.BLUE: self.MAX_CUBES,
            Colour.YELLOW: self.MAX_CUBES,
            Colour.BLACK: self.MAX_CUBES
        }

    def take_cubes(self, colour: Colour, qty: int):
        if colour not in self.cubes:
            raise Exception("Invalid colour specified.")

        if qty > self.cubes[colour]:
            raise DiseaseCubesDepletedException(colour.name.lower())
        self.cubes[colour] -= qty

    def return_cubes(self, colour: Colour, qty: int) -> None:
        if colour not in self.cubes:
            raise Exception("Invalid colour specified.")

        if self.cubes[colour] + qty > self.MAX_CUBES:
            raise Exception(f"Cannot return more than {self.MAX_CUBES} {colour.name.lower()} cubes to the pool.")
        self.cubes[colour] += qty