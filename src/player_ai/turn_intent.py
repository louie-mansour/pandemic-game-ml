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
        self.constraints = dict[City, list[ActionCost]]()
    
    # Undecided if we should reference the City of the PlayerLocationDeckCard here
    def add_possibility(self, city: City, action_cost: ActionCost):
        # Make sure this is covered in unit tests
        existing_action_costs = self.constraints.get(city)
        if not existing_action_costs:
            self.constraints[city] = [action_cost]
            return
            
        for existing_action_cost in existing_action_costs:
            if not bool(existing_action_cost.card) and existing_action_cost.actions <= action_cost.actions:
                return
        self.constraints[city] = [action_cost]

# Undecided if we should reference the City of the PlayerDeckCard here
class ActionCost():
    def __init__(self, actions: int, card: City | None = None):
        self.actions = actions
        self.card = card
