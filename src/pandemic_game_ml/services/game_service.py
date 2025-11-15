import logging
from ..exceptions.game_event_exceptions import EpidemicException
from ..models.player.player import Player
from ..models.board.board import Board
from ..models.shared.city import City
from ..models.player_deck.player_deck import PlayerDeck


class GameService:
    def __init__(self):
        pass

    def play_pandemic(self):
        board = Board()
        player_deck = PlayerDeck()
        atlanta_location = board.location_graph.locations.get(City.ATLANTA)
        assert atlanta_location is not None
        players = [Player(atlanta_location), Player(atlanta_location)]

        board.setup()
        for player in players:
            player.draw_cards_from_player_deck(player_deck, 4)
        player_deck.shuffle_epidemics_into_deck()

        turn = 0
        while True:
            for player in players:
                turn += 1
                logging.info(
                    f"\n--- Turn {turn}: Player at {player.location.city.name} ---"
                )
                player.take_turn()

                try:
                    player.draw_cards_from_player_deck(player_deck, 2)
                except EpidemicException:
                    board.handle_epidemic()
                board.take_turn()
