from Player import Player
from Dealer import Dealer
from Deck import Deck

class Game(object):

    def __init__(self):
        self.game_over = False
        self.player = Player()
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.start_game()

    def start_game(self):
        print 'Welcome to Blackjack Version 0.1.0'
        print 'Developed by Christian M. Brandalise'
        print '------------------------------------'
        player_name = raw_input('Please enter you name\n')

        try:
            self.player.set_name(player_name)
        except:
            print 'Error'
        else:
            self.game_loop()

    def check_for_21(self):
        pass

    def check_win(self):
        pass

    def game_loop(self):
        print 'Let\'s play some Blackjack!'

        print 'Dealing your hand'
        hand = self.dealer.deal_hand()
        print hand
        self.player.set_hand(hand)

        while not self.game_over:
            pass



g = Game()

