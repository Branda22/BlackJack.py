class Player(object):

    def __init__(self):
        self.name = ""
        self.hand = None

    def set_name(self, name):
        self.name = name

    def set_hand(self, hand):
        self.hand = hand

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = None


