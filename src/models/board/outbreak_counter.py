from src.models.game.game_state import GameState, GameLostReason


MAX_OUTBREAKS = 8

class OutbreakCounter:
    def __init__(self):
        self.count = 0

    def increment(self) -> GameState:
        if self.count >= MAX_OUTBREAKS:
            return GameState(GameState.LOST, GameLostReason.TOO_MANY_OUTBREAKS)
        self.count += 1
        return GameState(GameState.IN_PROGRESS)