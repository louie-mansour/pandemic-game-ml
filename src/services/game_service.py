import logging
from exceptions.game_event_exceptions import EpidemicException
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
            player.draw_cards_from_player_deck(player_deck, 4)
        player_deck.shuffle_epidemics_into_deck()

        turn = 0
        while True:
            for player in players:
                turn += 1
                logging.info(f"\n--- Turn {turn}: Player at {player.city.name} ---")
                player.take_turn()
            
                try:
                    player.draw_cards_from_player_deck(player_deck, 2)
                except EpidemicException:
                    board.handle_epidemic()
                board.take_turn()
    