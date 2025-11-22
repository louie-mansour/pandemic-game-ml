import unittest
import pytest
from models.player_deck.player_deck import PlayerDeck
import random


class TestInfectionDeck(unittest.TestCase):
    def test_initialize_infection_deck(self):
        infection_deck = PlayerDeck()
        assert len(infection_deck._deck) == 48

    def test_shuffle_is_deterministic_with_seed(self):
        state = random.getstate()
        try:
            random.seed(12345)
            deck1 = PlayerDeck()
            order1 = list(deck1._deck)

            random.seed(12345)
            deck2 = PlayerDeck()
            order2 = list(deck2._deck)
        finally:
            random.setstate(state)

        assert order1 == order2

    def test_shuffle_differs_with_different_seeds(self):
        state = random.getstate()
        try:
            random.seed(1)
            deck1 = PlayerDeck()
            order1 = list(deck1._deck)

            random.seed(2)
            deck2 = PlayerDeck()
            order2 = list(deck2._deck)
        finally:
            random.setstate(state)

        assert order1 != order2

    def test_draw_cards_default_draws_and_reduces_deck(self):
        deck = PlayerDeck()
        original_order = list(deck._deck)
        original_len = len(original_order)

        drawn = deck.draw_cards(2)
        assert len(drawn) == 2
        # Should draw the last two cards from the shuffled deck
        assert drawn[0] == original_order[-1]
        assert drawn[1] == original_order[-2]
        # Deck size reduced by one and remaining order preserved
        assert len(deck._deck) == original_len - 2
        assert deck._deck == original_order[:-2]

if __name__ == "__main__":
    unittest.main()

    