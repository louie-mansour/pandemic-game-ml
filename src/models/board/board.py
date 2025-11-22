import logging
from models.board.disease_cube_pool import DiseaseCubePool
from models.shared.colour import Colour
from models.shared.city import City
from models.board.infection_rate import InfectionRate
from models.map.location import Outbreak
from models.map.location_graph import LocationGraph
from models.board.outbreak_counter import OutbreakCounter
from models.infection_deck.infection_deck import InfectionDeck

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

    def take_turn(self):
        for _ in range(self.infection_rate.current_rate):
            city_to_infect = self.infection_deck.draw_card().value
            self._add_disease_cubes_to_location(city_to_infect, 1, city_to_infect.colour)
    
    def handle_epidemic(self):
        bottom_card = self.infection_deck.draw_bottom_card().value
        self._add_disease_cubes_to_location(bottom_card, 3, bottom_card.colour)
        self.infection_rate.increase()
        self.infection_deck.reshuffle_discard_pile_into_deck_on_top()

    def _add_disease_cubes_to_location(self, city: City, qty: int, colour: Colour):
        logging.info(f"Infecting {city.name} with {qty} {colour.name} disease cube(s)")
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

            self.outbreak_counter.increment()
            outbroken_cities.add(current_location.city)
            bfs_queue.extend(current_location.connections)
