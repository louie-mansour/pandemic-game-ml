from src.models.game.game_state import GameState
from src.models.player.player import Player
from src.models.board.board import Board
from src.models.shared.city import City
from src.models.player_deck.player_deck import PlayerDeck

class GameService:
    def __init__(self):
        pass

    def play_pandemic(self):
        board = Board()
        player_deck = PlayerDeck()
        players = [Player(City.ATLANTA), Player(City.ATLANTA)]

        board.setup()
        for player in players:
            player.draw_cards_from_player_deck(player_deck, 2)
        player_deck.shuffle_epidemics_into_deck()

        game_state = GameState(GameState.IN_PROGRESS)
        turn = 0
        while True:
            for player in players:
                turn += 1
                game_state = player.take_turn()
                if game_state.state != "in_progress":
                    return game_state
            
                game_state = player.draw_cards_from_player_deck(player_deck, 2)
                if game_state.state != "in_progress":
                    return game_state
            
            game_state = board.take_turn()
            if game_state.state != "in_progress":
                return game_state

            if game_state.state != "in_progress":
                return game_state
    
