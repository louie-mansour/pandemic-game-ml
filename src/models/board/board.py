from typing import Dict
from src.models.shared.city import City
from src.models.board.infection_rate import InfectionRate
from src.models.map.location import Location
from src.models.map.map_factory import LocationGraphFactory
from src.models.board.outbreak_counter import OutbreakCounter

NUMBER_OF_PLAYERS = 2

class Board:
    def __init__(self):
        self.location_graph: Dict[City, Location] = LocationGraphFactory.create_location_graph()
        self.outbreak_counter = OutbreakCounter()
        self.number_of_epidemics: int = 0
        self.infection_rate = InfectionRate()
        self.pawns: Dict[int, City] = {player_id: City.ATLANTA for player_id in range(NUMBER_OF_PLAYERS)}
