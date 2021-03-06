from random import randint

class Dealer(object):

    def __init__(self, deck, register=100):
        self.deck = deck
        self.register = register
        self.hand = None
        self.current_bet = 0

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

    def set_dealer_hand(self, hand):
        self.hand = hand

    def display_hand(self, oneCard):
        print 'The dealers hand'
        print '--------------------'
        for card in self.hand:
            print card.get_card_string()
            if oneCard:
                print 'XXXX'
                break
        print '\n'




