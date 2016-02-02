class Player(object):

    def __init__(self, cash=100):
        self.name = ""
        self.hand = None
        self.cash = cash

    def set_name(self, name):
        self.name = name

    def set_hand(self, hand):
        self.hand = hand

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = None

    def display_hand(self):
        print 'Your hand'
        print '--------------------'
        for card in self.hand:
            print card.get_card_string()
        print '\n'



