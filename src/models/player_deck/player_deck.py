from src.models.player_deck.player_deck_card import PlayerDeckCard
import random

NUMBER_OF_EPIDEMICS = 2

class PlayerDeck:
    def __init__(self):
        self._deck = [
            PlayerDeckCard.ALGIERS,
            PlayerDeckCard.ATLANTA,
            PlayerDeckCard.BAGHDAD,
            PlayerDeckCard.BANGKOK,
            PlayerDeckCard.BEIJING,
            PlayerDeckCard.BOGOTA,
            PlayerDeckCard.BUENOS_AIRES,
            PlayerDeckCard.CAIRO,
            PlayerDeckCard.CHENNAI,
            PlayerDeckCard.CHICAGO,
            PlayerDeckCard.DELHI,
            PlayerDeckCard.ESSEN,
            PlayerDeckCard.HO_CHI_MINH_CITY,
            PlayerDeckCard.HONG_KONG,
            PlayerDeckCard.ISTANBUL,
            PlayerDeckCard.JAKARTA,
            PlayerDeckCard.JOHANNESBURG,
            PlayerDeckCard.KARACHI,
            PlayerDeckCard.KHARTOUM,
            PlayerDeckCard.KINSHASA,
            PlayerDeckCard.KOLKATA,
            PlayerDeckCard.LAGOS,
            PlayerDeckCard.LIMA,
            PlayerDeckCard.LONDON,
            PlayerDeckCard.LOS_ANGELES,
            PlayerDeckCard.MADRID,
            PlayerDeckCard.MANILA,
            PlayerDeckCard.MELBOURNE,
            PlayerDeckCard.MEXICO_CITY,
            PlayerDeckCard.MIAMI,
            PlayerDeckCard.MILAN,
            PlayerDeckCard.MONTREAL,
            PlayerDeckCard.MOSCOW,
            PlayerDeckCard.MUMBAI,
            PlayerDeckCard.NEW_YORK,
            PlayerDeckCard.OSAKA,
            PlayerDeckCard.PARIS,
            PlayerDeckCard.RIYADH,
            PlayerDeckCard.SAN_FRANCISCO,
            PlayerDeckCard.SANTIAGO,
            PlayerDeckCard.SAO_PAULO,
            PlayerDeckCard.SEOUL,
            PlayerDeckCard.SHANGHAI,
            PlayerDeckCard.ST_PETERSBURG,
            PlayerDeckCard.SYDNEY,
            PlayerDeckCard.TAIPEI,
            PlayerDeckCard.TOKYO,
            PlayerDeckCard.WASHINGTON,
        ]
        self._epidemics = [PlayerDeckCard.EPIDEMIC] * NUMBER_OF_EPIDEMICS
        random.shuffle(self._deck)

    def draw_cards(self, num_cards: int = 1) -> list[PlayerDeckCard]:
        return [self._deck.pop() for _ in range(num_cards)]