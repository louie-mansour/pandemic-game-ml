from src.models.map.location import Location
from collections import deque

from src.models.map.location_graph import LocationGraph
from src.models.player.player import Player
from src.models.player_deck.player_deck_card import PlayerDeckCard
from src.player_ai.turn_intent import ActionCost, MovementPossibilities

class TurnOptions:
    @staticmethod
    def calculate_turn_options(player: Player, location_graph: LocationGraph) -> MovementPossibilities:
        # Find locations reachable by drive or ferry
        locations_can_drive_or_ferry_to = TurnOptions._locations_can_drive_or_ferry_to(player.location, ActionCost(0))

        # Find locations reachable by direct flight and then drive or ferry
        locations_can_direct_flight_to = TurnOptions._locations_can_direct_flight_to(player.hand)

        locations_can_direct_flight_drive_or_ferry_to = MovementPossibilities()
        for city, spent_costs in locations_can_direct_flight_to.possibilities.items():
            spent_cost = spent_costs[0]  # There should only be one action cost per city for direct flight
            locations_can_direct_flight_drive_or_ferry_to = locations_can_direct_flight_drive_or_ferry_to.merge(TurnOptions._locations_can_drive_or_ferry_to(location_graph.get_location_by_city(city), spent_cost))

        locations_can_direct_flight_drive_ferry_to = locations_can_direct_flight_to.merge(locations_can_drive_or_ferry_to)

        # Find all possible locations player can move to this turn
        charter_flight_possibilities = MovementPossibilities()
        for city, spent_costs in locations_can_direct_flight_drive_ferry_to.possibilities.items():
            if city not in map(lambda card: card.value, player.hand):
                # City card is not in player's hand
                continue
                
            # We should be finding the cheapest spent cost here
            # This is a simplification for now
            spent_cost = spent_costs[0]
            
            for city, _location in location_graph.locations.items():
                try:
                    charter_flight_possibilities.add_possibility(city, spent_cost.add_action(ActionCost(1, [city])))
                except ValueError:
                    # Overlapping cards, cannot add this possibility
                    continue
        return locations_can_direct_flight_drive_ferry_to.merge(charter_flight_possibilities)

    @staticmethod
    def _locations_can_drive_or_ferry_to(location: Location, spent_cost: ActionCost) -> MovementPossibilities:
        remaining_actions = 4 - spent_cost.actions
        visited = {location: 0}
        movementPossibilities = MovementPossibilities()
        result: dict[Location, int] = {location: 0}

        queue = deque([(location, 0)])

        while queue:
            current_location, distance = queue.popleft()
            
            if distance >= remaining_actions:
                continue
            
            for neighbor in current_location.connections:
                if neighbor not in visited:
                    visited[neighbor] = distance + 1
                    result[neighbor] = distance + 1
                    movementPossibilities.add_possibility(neighbor.city, ActionCost(distance + 1, spent_cost.cards))
                    queue.append((neighbor, distance + 1))
        return movementPossibilities
    
    @staticmethod
    def _locations_can_direct_flight_to(player_cards: list[PlayerDeckCard]) -> MovementPossibilities:
        movement_possibilities = MovementPossibilities()
        for card in player_cards:
            if card == PlayerDeckCard.EPIDEMIC:  # This is accidental complexity and can be improved with better types
                raise Exception("Epidemic card incorrectly included in player hand.")
            movement_possibilities.add_possibility(card.value, ActionCost(1, [card.value]))
        return movement_possibilities
