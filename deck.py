from card import Card

# Deck

import random

class Deck(object):

    def __init__(self):
        suits = ["C", "D", "H", "S"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            print(card)
