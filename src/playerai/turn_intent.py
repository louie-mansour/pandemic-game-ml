from dataclasses import dataclass
from enum import Enum

from models.shared.city import City

class TurnIntent(Enum):
    TREAT_DISEASE_WITH_CUBES_RUNNING_LOW = "treat_disease_with_cubes_running_low"
    TREAT_DISEASE_WITH_3_CUBES = "treat_disease_with_3_cubes"
    TREAT_NEARBY_DISEASE = "treat_nearby_disease"
    TREAT_DISEASE_WITH_2_CUBES = "treat_disease_with_2_cubes"
    TREAT_DISEASE_WITH_1_CUBE = "treat_disease_with_1_cube"
    MOVE_CLOSER_TO_DISEASE_LOCATIONS = "move_closer_to_disease_locations"

class TurnIntentWithCost():
    def __init__(self, intent: TurnIntent, action_cost: int):
        self.intent = intent
        self.action_cost = action_cost

class MovementPossibilities():
    def __init__(self):
        self.possibilities = dict[City, list[ActionCost]]()
    
    # Undecided if we should reference the City of the PlayerLocationDeckCard here
    def add_possibility(self, city: City, action_cost: ActionCost):
        # Make sure this is covered in unit tests
        existing_action_costs = self.possibilities.get(city)
        if not existing_action_costs:
            self.possibilities[city] = [action_cost]
            return
            
        for existing_action_cost in existing_action_costs:
            if not bool(existing_action_cost.cards) and existing_action_cost.actions <= action_cost.actions:
                return
        self.possibilities[city] = [action_cost]
    
    def merge(self, other: MovementPossibilities) -> MovementPossibilities:
        for city, action_costs in other.possibilities.items():
            for action_cost in action_costs:
                self.add_possibility(city, action_cost)
        return self

# Undecided if we should reference the City of the PlayerDeckCard here
@dataclass(frozen=True)
class ActionCost:
    actions: int
    cards: tuple[City, ...] = ()

    def add_action(self, other: ActionCost) -> ActionCost:
        if set(self.cards) & set(other.cards):
            raise ValueError("Cannot combine ActionCosts with overlapping cards")
        return ActionCost(self.actions + other.actions, tuple(list(self.cards) + list(other.cards)))