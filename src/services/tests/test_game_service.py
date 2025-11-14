import pytest
from exceptions.game_end_exceptions import TooManyOutbreaksException
from src.services.game_service import GameService


class TestGameService:

    def test_play_pandemic_initializes_and_runs(self):
        """Test that play_pandemic initializes game components and runs."""
        game_service = GameService()
        with pytest.raises(TooManyOutbreaksException):
            game_service.play_pandemic()