import pytest
from src.services.game_service import GameService
from src.models.game.game_state import GameState


class TestGameService:

    def test_play_pandemic_initializes_and_runs(self):
        """Test that play_pandemic initializes game components and runs."""
        game_service = GameService()
        result = game_service.play_pandemic()

        # Game should end in either won or lost
        assert result in [GameState.WON, GameState.LOST]