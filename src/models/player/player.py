import logging
from exceptions.game_end_exceptions import PlayerCardsDepletedException
from exceptions.game_event_exceptions import EpidemicException
from models.map.location import Location
from src.models.player_deck.player_deck_card import PlayerDeckCard
from src.models.player_deck.player_deck import PlayerDeck

HAND_LIMIT = 7

class Player:
    def __init__(self, location: Location):
        self.location: Location = location
        self.hand: list[PlayerDeckCard] = []

    def draw_cards_from_player_deck(self, player_deck: PlayerDeck, qty: int):
        cards = player_deck.draw_cards(qty)
        
        if len(cards) < qty:
            logging.info("Player deck is depleted")
            raise PlayerCardsDepletedException()

        epidemic_count = 0
        non_epidemic_cards = []
        for card in cards:
            if card == PlayerDeckCard.EPIDEMIC:
                epidemic_count += 1
                continue
            non_epidemic_cards.append(card)

        self.hand.extend(non_epidemic_cards)

        if (len(self.hand) > HAND_LIMIT):
            self.hand = self.hand[:HAND_LIMIT]

        if epidemic_count > 0:
            logging.info(f"{epidemic_count} epidemic card(s) drawn")
            raise EpidemicException(epidemic_count)
    
    def take_turn(self):
        pass

