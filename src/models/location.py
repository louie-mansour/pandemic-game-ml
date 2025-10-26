from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Set
from colour import Colour
from city import City

MAX_CUBES_PER_COLOUR = 3

class Outbreak(Enum):
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    BLACK = "black"
    NONE = "none"

@dataclass
class Location:
    city: City
    colour: Colour
    _connections: Set[Location] = field(init=False, repr=False, default_factory=set)

    _red_cubes_qty: int = field(default=0, init=False, repr=False)
    _blue_cubes_qty: int = field(default=0, init=False, repr=False)
    _yellow_cubes_qty: int = field(default=0, init=False, repr=False)
    _black_cubes_qty: int = field(default=0, init=False, repr=False)

    @property
    def connections(self) -> Set[Location]:
        """Return connected locations."""
        return self._connections

    def add_connection(self, other: Location) -> None:
        """Connect this location to another."""
        if other is self:
            return
        self._connections.add(other)
        other.add_connection(self)

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
