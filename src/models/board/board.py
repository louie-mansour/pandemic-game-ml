from src.models.board.disease_cube_pool import DiseaseCubePool
from src.models.game.game_state import GameState
from src.models.shared.colour import Colour
from src.models.shared.city import City
from src.models.board.infection_rate import InfectionRate
from src.models.map.location import Outbreak
from src.models.map.location_graph import LocationGraph
from src.models.board.outbreak_counter import OutbreakCounter
from src.models.infection_deck.infection_deck import InfectionDeck

class Board:
    def __init__(self):
        self.location_graph: LocationGraph = LocationGraph()
        self.outbreak_counter = OutbreakCounter()
        self.infection_rate = InfectionRate()
        self.infection_deck = InfectionDeck()
        self.disease_cube_pool = DiseaseCubePool()

    
    def setup(self):
        for _ in range(3):
            city_to_infect = self.infection_deck.draw_card().value
            self._add_disease_cubes_to_location(city_to_infect, 3, city_to_infect.colour)
        
        for _ in range(3):
            city_to_infect = self.infection_deck.draw_card().value
            self._add_disease_cubes_to_location(city_to_infect, 2, city_to_infect.colour)

        for _ in range(3):
            city_to_infect = self.infection_deck.draw_card().value
            self._add_disease_cubes_to_location(city_to_infect, 1, city_to_infect.colour)

    def take_turn(self) -> GameState:
        for _ in range(self.infection_rate.current_rate):
            city_to_infect = self.infection_deck.draw_card().value
            game_state = self._add_disease_cubes_to_location(city_to_infect, 1, city_to_infect.colour)
            if game_state.state != "in_progress":
                return game_state
        return GameState(GameState.IN_PROGRESS)

    def _add_disease_cubes_to_location(self, city: City, qty: int, colour: Colour) -> GameState:
        location = self.location_graph.get_location_by_city(city)
        bfs_queue = [location]
        outbroken_cities = set[City]()

        while bfs_queue:
            current_location = bfs_queue.pop(0)
            outbreak = current_location.add_cubes(self.disease_cube_pool, qty, colour)
            qty = 1 # Subsequent outbreaks only add 1 cube to connected cities
            if outbreak == Outbreak.NONE:
                continue
        
            if outbroken_cities.__contains__(current_location.city):
                continue

            game_state = self.outbreak_counter.increment()
            if game_state == GameState.LOST:
                return game_state
            outbroken_cities.add(current_location.city)
            bfs_queue.extend(current_location.connections)
        return GameState(GameState.IN_PROGRESS)
