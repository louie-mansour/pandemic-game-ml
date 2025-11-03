from src.models.game.game_state import GameLostReason, GameState
from src.models.shared.city import City
from src.models.shared.colour import Colour
from src.models.board.outbreak_counter import OutbreakCounter
from src.models.map.location import Location


class OutbreakResolver:
    
    @staticmethod
    def resolve_outbreak(location: Location, colour: Colour, outbreak_counter: OutbreakCounter) -> GameState:
        # Track cities that have already outbroken this chain
        outbroken_cities = set[City]()
        bfs_queue = [location]
        while bfs_queue:
            current_location = bfs_queue.pop(0)
            if current_location in outbroken_cities:
                continue
            outbroken_cities.add(current_location.city)
            if outbreak_counter.increment() == GameState.LOST:
                return GameState(GameState.LOST, GameLostReason.TOO_MANY_OUTBREAKS)

            for neighbor in current_location.connections:
                bfs_queue.append(neighbor)
            