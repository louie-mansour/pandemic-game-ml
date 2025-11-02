from models.board.disease_cube_pool import DiseaseCubePool
from src.models.shared.colour import Colour
from src.models.shared.city import City
from src.models.board.infection_rate import InfectionRate
from src.models.map.location import Location, Outbreak
from models.map.location_graph import LocationGraph
from src.models.board.outbreak_counter import OutbreakCounter

NUMBER_OF_PLAYERS = 2

class Board:
    def __init__(self):
        self.location_graph: LocationGraph = LocationGraph()
        self.outbreak_counter = OutbreakCounter()
        self.disease_cube_pool = DiseaseCubePool()
        # self.number_of_epidemics: int = 0
        # self.infection_rate = InfectionRate()
    
    def add_disease_cubes_to_location(self, city, qty: int, colour: Colour) -> Outbreak:
        location = self.location_graph.get_location_by_city(city)
        outbreak = self._add_cubes_from_pool(colour, qty, location)

        if(outbreak == Outbreak.NONE):
            return Outbreak.NONE
        
        self.outbreak_counter.increment()
        return outbreak
        # TODO: outbreak chain handling


    def _add_cubes_from_pool(self, colour: Colour, qty: int, location: Location) -> Outbreak:
        if colour == Colour.RED:
            self.disease_cube_pool.take_cubes(Colour.RED, qty)
            return location.add_red_cubes(qty)
        elif colour == Colour.BLUE:
            self.disease_cube_pool.take_cubes(Colour.BLUE, qty)
            return location.add_blue_cubes(qty)
        elif colour == Colour.YELLOW:
            self.disease_cube_pool.take_cubes(Colour.YELLOW, qty)
            return location.add_yellow_cubes(qty)
        elif colour == Colour.BLACK:
            self.disease_cube_pool.take_cubes(Colour.BLACK, qty)
            return location.add_black_cubes(qty)
        else:
            raise Exception("Invalid colour specified.")