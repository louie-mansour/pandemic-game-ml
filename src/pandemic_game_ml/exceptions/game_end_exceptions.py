from enum import Enum

class GameResult(Enum):
    WON = "won"
    LOST = "lost"


class GameEndException(Exception):
    def __init__(self, result: GameResult, reason: str):
        self.result = result
        self.reason = reason
        message = f"Game {result.value}: {reason}"
        super().__init__(message)


class GameWonException(GameEndException):
    def __init__(self):
        super().__init__(result=GameResult.WON, reason="All diseases cured")


class GameLostException(GameEndException):
    def __init__(self, reason: str):
        super().__init__(result=GameResult.LOST, reason=reason)


class DiseaseCubesDepletedException(GameLostException):
    def __init__(self, color: str):
        self.color = color
        super().__init__(f"Ran out of {color} disease cubes")


class PlayerCardsDepletedException(GameLostException):
    def __init__(self):
        super().__init__("Ran out of player cards")


class TooManyOutbreaksException(GameLostException):
    def __init__(self, outbreak_count: int):
        self.outbreak_count = outbreak_count
        super().__init__(f"Too many outbreaks: {outbreak_count}")