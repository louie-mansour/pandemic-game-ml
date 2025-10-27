from __future__ import annotations
from enum import Enum
from typing import Set
from models.board.disease_cube_pool import DiseaseCubePool
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
    def __init__(self, city: City):
        self.city = city
        self._connections: Set[Location] = set()
        self._red_cubes_qty: int = 0
        self._blue_cubes_qty: int = 0
        self._yellow_cubes_qty: int = 0
        self._black_cubes_qty: int = 0

    @property
    def connections(self) -> Set[Location]:
        return self._connections

    def add_connections(self, *others: Location) -> None:
        self._connections.update(others)

    def _add_cubes(self, qty: int, cube_type: str) -> Outbreak:
        cube_qty_attr = f"_{cube_type}_cubes_qty"
        current_qty = getattr(self, cube_qty_attr)
        
        if current_qty + qty <= MAX_CUBES_PER_COLOUR:
            setattr(self, cube_qty_attr, current_qty + qty)
            return Outbreak.NONE
            
        setattr(self, cube_qty_attr, MAX_CUBES_PER_COLOUR)
        for location in self._connections:
            getattr(location, f"add_{cube_type}_cubes")(1)
        return getattr(Outbreak, cube_type.upper())

    def add_red_cubes(self, qty: int) -> Outbreak:
        return self._add_cubes(qty, "red")
    
    def add_blue_cubes(self, qty: int) -> Outbreak:
        return self._add_cubes(qty, "blue")
    
    def add_yellow_cubes(self, qty: int) -> Outbreak:
        return self._add_cubes(qty, "yellow")
    
    def add_black_cubes(self, qty: int) -> Outbreak:
        return self._add_cubes(qty, "black")
