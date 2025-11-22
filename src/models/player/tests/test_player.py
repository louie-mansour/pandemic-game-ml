import pytest
from exceptions.game_end_exceptions import PlayerCardsDepletedException
from exceptions.game_event_exceptions import EpidemicException
from models.player_deck.player_deck_card import PlayerDeckCard
from models.player_deck.player_deck import PlayerDeck
from models.shared.city import City
from models.player.player import Player
from models.board.board import LocationGraph

@pytest.fixture(scope="module", autouse=True)
def location_graph():
    return LocationGraph()

def test_initialize_player(location_graph):
    player = Player(location_graph.get_location_by_city(City.ATLANTA))
    assert player.location.city == City.ATLANTA
    assert player.hand == []


def test_draw_card_from_player_deck(location_graph):
    player = Player(location_graph.get_location_by_city(City.ATLANTA))
    player_deck = PlayerDeck()
    player.draw_cards_from_player_deck(player_deck, 2)
    assert len(player.hand) == 2

def test_draw_single_epidemic_card(location_graph):
    player = Player(location_graph.get_location_by_city(City.ATLANTA))
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.EPIDEMIC, PlayerDeckCard.ATLANTA]
    with pytest.raises(EpidemicException):
        player.draw_cards_from_player_deck(player_deck, 2)
    assert len(player.hand) == 1
    assert PlayerDeckCard.EPIDEMIC not in player.hand


def test_draw_double_epidemic_card(location_graph):
    player = Player(location_graph.get_location_by_city(City.ATLANTA))
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.EPIDEMIC, PlayerDeckCard.EPIDEMIC]
    with pytest.raises(EpidemicException):
        player.draw_cards_from_player_deck(player_deck, 2)
    assert len(player.hand) == 0


def test_draw_cards_exceeding_hand_limit(location_graph):
    player = Player(location_graph.get_location_by_city(City.ATLANTA))
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.ATLANTA] * 10
    player.draw_cards_from_player_deck(player_deck, 10)
    assert len(player.hand) == 7


def test_draw_cards_when_deck_empty(location_graph):
    player = Player(location_graph.get_location_by_city(City.ATLANTA))
    player_deck = PlayerDeck()
    player_deck._deck = []
    with pytest.raises(PlayerCardsDepletedException):
        player.draw_cards_from_player_deck(player_deck, 2)



def test_draw_cards_when_deck_has_insufficient_cards(location_graph):
    player = Player(location_graph.get_location_by_city(City.ATLANTA))
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.ATLANTA]
    with pytest.raises(PlayerCardsDepletedException):
        player.draw_cards_from_player_deck(player_deck, 2)