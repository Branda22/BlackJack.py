from Card import Card


class Deck(object):

    card_suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    card_rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self):
        self.deck = []

        for suit in Deck.card_suit:
            for rank in Deck.card_rank:
                c = Card(suit, rank)
                self.deck.append(c)

        print self.deck


d = Deck()