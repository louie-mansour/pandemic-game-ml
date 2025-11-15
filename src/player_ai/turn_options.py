from models.map import location
from models.map.location import Location
from collections import deque

from models.player_deck.player_deck_card import PlayerDeckCard
from player_ai.turn_intent import ActionCost, MovementPossibilities

class TurnOptions:
    @staticmethod
    def locations_can_drive_or_ferry_to(location: Location) -> MovementPossibilities:
        visited = {location: 0}
        movementPossibilities = MovementPossibilities()
        result: dict[Location, int] = {location: 0}

        queue = deque([(location, 0)])

        while queue:
            current_location, distance = queue.popleft()
            
            if distance >= 4:
                continue
            
            for neighbor in current_location.connections:
                if neighbor not in visited:
                    visited[neighbor] = distance + 1
                    result[neighbor] = distance + 1
                    movementPossibilities.add_possibility(neighbor.city, ActionCost(distance + 1))
                    queue.append((neighbor, distance + 1))
        return movementPossibilities
    
    @staticmethod
    def locations_can_direct_flight_to(player_cards: list[PlayerDeckCard]) -> MovementPossibilities:
        movementPossibilities = MovementPossibilities()
        for card in player_cards:
            if card == PlayerDeckCard.EPIDEMIC:  # This is accidental complexity and can be improved with better types
                raise Exception("Epidemic card incorrectly included in player hand.")
            movementPossibilities.add_possibility(card.value, ActionCost(1, card.value))
        return movementPossibilities

    @staticmethod
    def locations_can_charter_flight_to(player_card: PlayerDeckCard, location: Location) -> MovementPossibilities:
        movementPossibilities = MovementPossibilities()
        if player_card == PlayerDeckCard.EPIDEMIC:  # This is accidental complexity
            raise Exception("Epidemic card incorrectly included in player hand.")
        if player_card.value == location.city:
            movementPossibilities.add_possibility(player_card.value, ActionCost(1, player_card.value))
        return movementPossibilities