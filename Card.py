class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_card(self):
        return (self.rank, self.suit)

    def get_card_string(self):
        return self.rank + ' of ' + self.suit
