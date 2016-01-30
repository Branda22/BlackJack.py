from Player import Player
from Dealer import Dealer
from Deck import Deck

class Game(object):

    def __init__(self):
        self.game_over = False
        self.player = Player()
        self.deck = Deck()
        self.dealer = Dealer(self.deck)

    def start_game(self):
        pass

    def game_loop(self):
        while not self.game_over:
            pass



g = Game()

