from random import randint
from Card import Card


class Deck(object):

    card_suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    card_rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self):
        self.deck = []
        self.new_deck()

    def new_deck(self):
        for suit in Deck.card_suit:
            for rank in Deck.card_rank:
                c = Card(suit, rank)
                self.deck.append(c)

    def print_cards_in_deck(self):
        for card in self.deck:
            print '{card}'.format(card=card.get_card_string())

    def insert_card(self, card):
        self.deck.append(card)

    def remove_last_card(self):
        return self.deck.pop()

    def remove_card_at_index(self, idx):
        return self.deck.pop(idx)

