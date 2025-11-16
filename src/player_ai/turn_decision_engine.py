from models.map.location_graph import LocationGraph
from src.models.player.player import Player
from src.player_ai.turn_intent import MovementPossibilities
from src.player_ai.turn_options import TurnOptions

class TurnDecisionEngine:

    @staticmethod
    def determine_turn_options(player: Player, location_graph: LocationGraph) -> MovementPossibilities:
        return TurnOptions.calculate_turn_options(player, location_graph)