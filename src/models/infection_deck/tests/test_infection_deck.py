import unittest
import pytest
from src.models.infection_deck.infection_deck import InfectionDeck
import random


class TestInfectionDeck(unittest.TestCase):
    def test_initialize_infection_deck(self):
        infection_deck = InfectionDeck()
        assert len(infection_deck._deck) == 48

    def test_shuffle_is_deterministic_with_seed(self):
        state = random.getstate()
        try:
            random.seed(12345)
            deck1 = InfectionDeck()
            order1 = list(deck1._deck)

            random.seed(12345)
            deck2 = InfectionDeck()
            order2 = list(deck2._deck)
        finally:
            random.setstate(state)

        assert order1 == order2

    def test_shuffle_differs_with_different_seeds(self):
        state = random.getstate()
        try:
            random.seed(1)
            deck1 = InfectionDeck()
            order1 = list(deck1._deck)

            random.seed(2)
            deck2 = InfectionDeck()
            order2 = list(deck2._deck)
        finally:
            random.setstate(state)

        assert order1 != order2

    def test_draw_cards_default_draws_one_and_reduces_deck(self):
        deck = InfectionDeck()
        original_order = list(deck._deck)
        original_len = len(original_order)

        drawn = deck.draw_card()
        # Should draw the last card from the shuffled deck
        assert drawn == original_order[-1]
        # Deck size reduced by one and remaining order preserved
        assert len(deck._deck) == original_len - 1
        assert deck._deck == original_order[:-1]

    def test_draw_bottom_card_draws_first_and_reduces_deck(self):
        deck = InfectionDeck()
        original_order = list(deck._deck)

        bottom = deck.draw_bottom_card()
        assert bottom == original_order[0]
        assert len(deck._deck) == len(original_order) - 1
        assert deck._deck == original_order[1:]

    def test_draw_bottom_card_multiple_returns_expected_sequence(self):
        deck = InfectionDeck()
        original_order = list(deck._deck)

        n = 5
        drawn = [deck.draw_bottom_card() for _ in range(n)]
        assert drawn == original_order[:n]
        assert deck._deck == original_order[n:]

    def test_draw_bottom_card_on_empty_deck_raises_index_error(self):
        deck = InfectionDeck()
        for _ in range(48):
            deck.draw_bottom_card()
        assert len(deck._deck) == 0
        with pytest.raises(IndexError):
            deck.draw_bottom_card()
    
    def test_draw_card_adds_to_discard_pile(self):
        deck = InfectionDeck()
        assert len(deck._discard) == 0
        
        drawn = deck.draw_card()
        assert len(deck._discard) == 1
        assert deck._discard[0] == drawn

    def test_draw_bottom_card_adds_to_discard_pile(self):
        deck = InfectionDeck()
        assert len(deck._discard) == 0
        
        drawn = deck.draw_bottom_card()
        assert len(deck._discard) == 1
        assert deck._discard[0] == drawn

    def test_multiple_draws_build_discard_pile(self):
        deck = InfectionDeck()
        drawn_cards = []
        
        for _ in range(5):
            drawn_cards.append(deck.draw_card())
        
        assert len(deck._discard) == 5
        assert deck._discard == drawn_cards

    def test_reshuffle_discard_pile_clears_discard(self):
        deck = InfectionDeck()
        for _ in range(10):
            deck.draw_card()
        
        assert len(deck._discard) == 10
        deck.reshuffle_discard_pile_into_deck_on_top()
        assert len(deck._discard) == 0

    def test_reshuffle_discard_pile_adds_cards_to_deck(self):
        deck = InfectionDeck()
        initial_deck_size = len(deck._deck)
        
        for _ in range(10):
            deck.draw_card()
        
        assert len(deck._deck) == initial_deck_size - 10
        deck.reshuffle_discard_pile_into_deck_on_top()
        assert len(deck._deck) == initial_deck_size

    def test_reshuffle_discard_pile_preserves_all_cards(self):
        deck = InfectionDeck()
        drawn_cards = []
        
        for _ in range(10):
            drawn_cards.append(deck.draw_card())
        
        deck.reshuffle_discard_pile_into_deck_on_top()
        
        # All drawn cards should be back in the deck
        for card in drawn_cards:
            assert card in deck._deck

    def test_reshuffle_discard_pile_shuffles_discards(self):
        state = random.getstate()
        try:
            random.seed(999)
            deck = InfectionDeck()
            for _ in range(10):
                deck.draw_card()
            discard_order = list(deck._discard)
            
            deck.reshuffle_discard_pile_into_deck_on_top()
            top_10_cards = deck._deck[-10:]
            
            # After shuffle, order should differ from original discard order
            assert top_10_cards != discard_order
        finally:
            random.setstate(state)

    def test_reshuffle_empty_discard_pile_no_change(self):
        deck = InfectionDeck()
        original_deck = list(deck._deck)
        
        deck.reshuffle_discard_pile_into_deck_on_top()
        
        assert deck._deck == original_deck
        assert len(deck._discard) == 0

    def test_reshuffle_discard_pile_adds_cards_to_top_of_deck(self):
        deck = InfectionDeck()
        # Draw some cards to build discard pile
        for _ in range(5):
            deck.draw_card()
        
        discard_cards = set(deck._discard)
        remaining_deck_size = len(deck._deck)
        
        deck.reshuffle_discard_pile_into_deck_on_top()
        
        # The last 5 cards in the deck should be from the discard pile
        top_5_cards = deck._deck[-5:]
        assert all(card in discard_cards for card in top_5_cards)
        
        # The first cards should be from the original remaining deck
        # (not from discard pile)
        bottom_cards = deck._deck[:remaining_deck_size]
        assert len(bottom_cards) == remaining_deck_size

if __name__ == "__main__":
    unittest.main()

    