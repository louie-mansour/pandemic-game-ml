from __future__ import annotations
from enum import Enum
from typing import Set
from src.models.board.disease_cube_pool import DiseaseCubePool
from src.models.shared.colour import Colour
from src.models.shared.city import City

MAX_CUBES_PER_COLOUR = 3

class Outbreak(Enum):
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    BLACK = "black"
    NONE = "none"

class Location:
    def __init__(self, city: City, disease_pool: DiseaseCubePool):
        self.city = city
        self._disease_pool = disease_pool
        self._connections: Set[Location] = set()
        self.cubes = {
            Colour.RED: 0,
            Colour.BLUE: 0,
            Colour.YELLOW: 0,
            Colour.BLACK: 0
        }

    @property
    def connections(self) -> Set[Location]:
        return self._connections

    def add_connections(self, *others: Location) -> None:
        self._connections.update(others)

    def add_cubes(self, qty: int, colour: Colour) -> Outbreak:
        if colour not in self.cubes:
            raise Exception("Invalid colour specified.")

        current_cubes = self.cubes[colour]
        if current_cubes + qty > MAX_CUBES_PER_COLOUR:
            self._disease_pool.take_cubes(colour, MAX_CUBES_PER_COLOUR - current_cubes)
            self.cubes[colour] = MAX_CUBES_PER_COLOUR
            return Outbreak(colour.value)

        self.cubes[colour] += qty
        self._disease_pool.take_cubes(colour, qty)
        return Outbreak.NONE
    
    def remove_cube(self, colour: Colour) -> None:
        if colour not in self.cubes:
            raise Exception("Invalid colour specified.")

        if self.cubes[colour] == 0:
            raise Exception(f"No {colour.name.lower()} cubes to remove from this location.")

        self.cubes[colour] -= 1
        self._disease_pool.return_cubes(colour, 1)