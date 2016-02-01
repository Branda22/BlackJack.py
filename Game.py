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

    def check_win(self, player_hand, dealer_hand):
        if self.check_hand_value(player_hand) > self.check_hand_value(dealer_hand):
            return True
        else:
            return False

    def hit(self):
        card = self.dealer.deal_card()
        self.player.add_card_to_hand(card)

    def stop(self):
        pass

    def check_hand_value(self, hand):
        total = 0
        for card in hand:
            if card.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                total += int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                total += 10
            else:
                c_ace = total
                c_ace += 11
                if c_ace > 21:
                    total += 1
                else:
                    total += 11

        return total

    def check_bust(self, hand):
        if self.check_hand_value(hand) > 21:
            return True
        else:
            return False

    def game_loop(self):
        print 'Let\'s play some Blackjack!'

        print 'Dealing your hand'
        hand = self.dealer.deal_hand(2)
        print hand
        self.player.set_hand(hand)
        print 'Dealing dealers hand'
        dhand = self.dealer.deal_hand(2)
        self.dealer.set_dealer_hand(dhand)

        while not self.game_over:
            print 'Your hand'
            print '--------------------'
            self.player.display_hand()
            print '\n'
            print 'The dealers hand'
            print '--------------------'
            self.dealer.display_hand(True)
            print 'What would you like to do?'
            print '1. HIT'
            print '2. STOP'
            choice = int(raw_input())

            if choice in range(1,4):
                if choice == 1:
                    self.hit()
                    self.player.display_hand()
                    if self.check_bust(self.player.hand):
                        print 'You busted!'
                        self.game_over = True

                elif choice == 2:
                    print 'Let\'s see who won!'
                    if self.check_win(self.player.hand, self.dealer.hand):
                        print "Blackjack! Congratulations"
                    else:
                        print "The dealer has won"

                    self.game_over = True

        else:
            print 'The game has ended my dear'
            print 'Would you like to play again?'

g = Game()

