from src.models.infection_deck.infection_deck_card import InfectionDeckCard
import random


class InfectionDeck:
    def __init__(self):
        self._deck = [
            InfectionDeckCard.ALGIERS,
            InfectionDeckCard.ATLANTA,
            InfectionDeckCard.BAGHDAD,
            InfectionDeckCard.BANGKOK,
            InfectionDeckCard.BEIJING,
            InfectionDeckCard.BOGOTA,
            InfectionDeckCard.BUENOS_AIRES,
            InfectionDeckCard.CAIRO,
            InfectionDeckCard.CHENNAI,
            InfectionDeckCard.CHICAGO,
            InfectionDeckCard.DELHI,
            InfectionDeckCard.ESSEN,
            InfectionDeckCard.HO_CHI_MINH_CITY,
            InfectionDeckCard.HONG_KONG,
            InfectionDeckCard.ISTANBUL,
            InfectionDeckCard.JAKARTA,
            InfectionDeckCard.JOHANNESBURG,
            InfectionDeckCard.KARACHI,
            InfectionDeckCard.KHARTOUM,
            InfectionDeckCard.KINSHASA,
            InfectionDeckCard.KOLKATA,
            InfectionDeckCard.LAGOS,
            InfectionDeckCard.LIMA,
            InfectionDeckCard.LONDON,
            InfectionDeckCard.LOS_ANGELES,
            InfectionDeckCard.MADRID,
            InfectionDeckCard.MANILA,
            InfectionDeckCard.MELBOURNE,
            InfectionDeckCard.MEXICO_CITY,
            InfectionDeckCard.MIAMI,
            InfectionDeckCard.MILAN,
            InfectionDeckCard.MONTREAL,
            InfectionDeckCard.MOSCOW,
            InfectionDeckCard.MUMBAI,
            InfectionDeckCard.NEW_YORK,
            InfectionDeckCard.OSAKA,
            InfectionDeckCard.PARIS,
            InfectionDeckCard.RIYADH,
            InfectionDeckCard.SAN_FRANCISCO,
            InfectionDeckCard.SANTIAGO,
            InfectionDeckCard.SAO_PAULO,
            InfectionDeckCard.SEOUL,
            InfectionDeckCard.SHANGHAI,
            InfectionDeckCard.ST_PETERSBURG,
            InfectionDeckCard.SYDNEY,
            InfectionDeckCard.TAIPEI,
            InfectionDeckCard.TOKYO,
            InfectionDeckCard.WASHINGTON,
        ]
        random.shuffle(self._deck)

    def draw_card(self) -> InfectionDeckCard:
        return self._deck.pop()

    def draw_bottom_card(self) -> InfectionDeckCard:
        return self._deck.pop(0)