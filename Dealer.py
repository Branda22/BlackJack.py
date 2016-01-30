from Deck import Deck

class Dealer(object):

    def __init__(self, deck, register=100):
        self.deck = Deck()
        self.register = register

    def deal_hand(self, num_cards):
        hand = []
        for i in xrange(0, num_cards):
            idx = randint(0, len(self.deck))
            card = self.deck.remove_card_at_index(idx)
            hand.append(card)
        return hand

    def deal_card(self):
        idx = randint(0, len(self.deck))
        return self.deck.remove_card_at_index(idx)

