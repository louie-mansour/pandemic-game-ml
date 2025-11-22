from enum import Enum

class GameLostReason(Enum):
    OUT_OF_CUBES = "out_of_cubes"
    TOO_MANY_OUTBREAKS = "too_many_outbreaks"
    OUT_OF_PLAYER_CARDS = "out_of_player_cards"
    NONE = "none"

class GameState:
    IN_PROGRESS = "in_progress"
    WON = "won"
    LOST = "lost"
    EPIDEMIC = "epidemic"
    DOUBLE_EPIDEMIC = "double_epidemic"

    def __init__(self, state: str, lose_reason: GameLostReason = GameLostReason.NONE):
        self.state = state
        self.lose_reason = lose_reason

    def __eq__(self, other):
        if not isinstance(other, GameState):
            return False
        return self.state == other.state
    
    def __repr__(self):
        return f"GameState(state={self.state!r}, lose_reason={self.lose_reason!r})"