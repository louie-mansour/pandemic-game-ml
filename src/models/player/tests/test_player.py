import pytest
from exceptions.game_end_exceptions import PlayerCardsDepletedException
from exceptions.game_event_exceptions import EpidemicException
from src.models.player_deck.player_deck_card import PlayerDeckCard
from src.models.player_deck.player_deck import PlayerDeck
from src.models.shared.city import City
from src.models.player.player import Player

def test_initialize_player():
    player = Player(City.ATLANTA)
    assert player.city == City.ATLANTA
    assert player.hand == []


def test_draw_card_from_player_deck():
    player = Player(City.ATLANTA)
    player_deck = PlayerDeck()
    player.draw_cards_from_player_deck(player_deck, 2)
    assert len(player.hand) == 2

def test_draw_single_epidemic_card():
    player = Player(City.ATLANTA)
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.EPIDEMIC, PlayerDeckCard.ATLANTA]
    with pytest.raises(EpidemicException):
        player.draw_cards_from_player_deck(player_deck, 2)
    assert len(player.hand) == 1
    assert PlayerDeckCard.EPIDEMIC not in player.hand


def test_draw_double_epidemic_card():
    player = Player(City.ATLANTA)
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.EPIDEMIC, PlayerDeckCard.EPIDEMIC]
    with pytest.raises(EpidemicException):
        player.draw_cards_from_player_deck(player_deck, 2)
    assert len(player.hand) == 0


def test_draw_cards_exceeding_hand_limit():
    player = Player(City.ATLANTA)
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.ATLANTA] * 10
    player.draw_cards_from_player_deck(player_deck, 10)
    assert len(player.hand) == 7


def test_draw_cards_when_deck_empty():
    player = Player(City.ATLANTA)
    player_deck = PlayerDeck()
    player_deck._deck = []
    with pytest.raises(PlayerCardsDepletedException):
        player.draw_cards_from_player_deck(player_deck, 2)



def test_draw_cards_when_deck_has_insufficient_cards():
    player = Player(City.ATLANTA)
    player_deck = PlayerDeck()
    player_deck._deck = [PlayerDeckCard.ATLANTA]
    with pytest.raises(PlayerCardsDepletedException):
        player.draw_cards_from_player_deck(player_deck, 2)