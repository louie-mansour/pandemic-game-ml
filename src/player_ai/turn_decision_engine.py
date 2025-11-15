from src.models.map.location import Location
from src.player_ai.turn_intent import MovementPossibilities
from src.player_ai.turn_options import TurnOptions

class TurnDecisionEngine:

    @staticmethod
    def determine_turn_options(location: Location) -> MovementPossibilities:
        locations_can_drive_or_ferry_to = TurnOptions.locations_can_drive_or_ferry_to(location)
        return locations_can_drive_or_ferry_to
    