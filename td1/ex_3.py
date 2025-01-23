# Je n'ai pas la dernière version de python d'installée donc les listes ne sont pas typées

import random
from typing import Union

SUITE_DIAMONDS = "D"
SUITE_HEART = "H"
SUITE_CLUBS = "C"
SUITE_SPADES = "S"

class Card:

    VALUE_TO_NAME = {
        1 : "As",
        2 : "2",
        3 : "3",
        4 : "4",
        5 : "5",
        6 : "6",
        7 : "7",
        8 : "8",
        9 : "9",
        10 : "10",
        11 : "Valet",
        12 : "Reine",
        13 : "Roi",
    }

    SUITE_TO_NAME = {
        SUITE_HEART : "coeur",
        SUITE_DIAMONDS : "carreau",
        SUITE_CLUBS : "trêfle",
        SUITE_SPADES : "pique",
    }

    def __init__(self, suite:str, value:int) -> None:
        if value not in range(1,13):
            raise Exception("Range of value must be between 1 and 13")
        if suite not in (SUITE_DIAMONDS, SUITE_SPADES, SUITE_CLUBS, SUITE_HEART):
            raise Exception("Invalid suite for card")
        self.suite = suite
        self.value = value

    def get_nom(self) -> str:
        return f"{Card.VALUE_TO_NAME[self.value]} de {Card.SUITE_TO_NAME[self.suite]}"

class Deck:

    def __init__(self) -> None:
        self.cards : list = []
        for value in range(1, 13):
            for suite in (SUITE_CLUBS, SUITE_DIAMONDS, SUITE_HEART, SUITE_SPADES):
                self.cards.append(Card(suite, value))

    def shuffle(self, newDeck:list=[]) -> None:
        rand = random.randint(0, len(self.cards) - 1)
        newDeck.append(self.cards.pop(rand))
        if len(self.cards) > 0:
            self.shuffle(newDeck)
        else:
            self.cards = newDeck

    def afficher(self) -> None:
        for card in self.cards:
            print(card.get_nom())

    def tirer(self) -> Union[Card, None]:
        return self.cards.pop()
            

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.afficher()
    while len(deck.cards) > 0:
        deck.tirer()


