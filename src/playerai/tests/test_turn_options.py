import pytest
from models.map.location_graph import LocationGraph
from playerai.turn_intent import ActionCost, MovementPossibilities
from playerai.turn_options import TurnOptions
from models.shared.city import City

class TestTurnOptions:

    def test_locations_can_drive_ferry_to(self):

        assert True
        location_graph = LocationGraph()
        zero_actions = ActionCost(0)
        atlanta_location = location_graph.get_location_by_city(City.ATLANTA)

        movement_possibilities = TurnOptions._locations_can_drive_or_ferry_to(atlanta_location, zero_actions)
        expected_movement_possibilities = MovementPossibilities()
        expected_movement_possibilities.add_possibility(City.ATLANTA, ActionCost(0))
        expected_movement_possibilities.add_possibility(City.CHICAGO, ActionCost(1))
        expected_movement_possibilities.add_possibility(City.MIAMI, ActionCost(1))
        expected_movement_possibilities.add_possibility(City.WASHINGTON, ActionCost(1))
        expected_movement_possibilities.add_possibility(City.MEXICO_CITY, ActionCost(2))
        expected_movement_possibilities.add_possibility(City.LOS_ANGELES, ActionCost(3))
        expected_movement_possibilities.add_possibility(City.SAN_FRANCISCO, ActionCost(3))
        expected_movement_possibilities.add_possibility(City.MONTREAL, ActionCost(3))

        assert movement_possibilities.possibilities == expected_movement_possibilities.possibilities