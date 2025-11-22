from models.map.location_graph import LocationGraph
from models.player.player import Player
from playerai.turn_intent import MovementPossibilities
from playerai.turn_options import TurnOptions

class TurnDecisionEngine:

    @staticmethod
    def determine_turn_options(player: Player, location_graph: LocationGraph) -> MovementPossibilities:
        return TurnOptions.calculate_turn_options(player, location_graph)