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

    def set_bet(self):
        bet = raw_input('Please enter your bet from 1 to {cash}'.format(cash=self.player.cash))
        try:
            bet = int(bet)
        except:
            print 'You did not enter a number.'

        if bet in range(1, self.player.cash + 1):
            self.player.cash -= bet
            self.dealer.current_bet += bet

    def display_balance(self):
        print 'Your balance \n'
        print self.player.cash
        print 'Dealers balance \n'
        print self.dealer.register

    def check_win(self, player_hand, dealer_hand):
        if self.check_hand_value(player_hand) > self.check_hand_value(dealer_hand):
            return True
        else:
            return False

    def hit(self):
        card = self.dealer.deal_card()
        self.player.add_card_to_hand(card)

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

    def award_bet(self, to_who):
        if to_who == 'dealer':
            self.dealer.register += self.dealer.current_bet
            self.dealer.current_bet = 0
        else:
            winning = self.dealer.current_bet * 2
            self.dealer.register -= winning
            self.player.cash += winning


    def game_loop(self):
        print 'Let\'s play some Blackjack!'
        self.set_bet()
        self.display_balance()
        print '********* Dealing your hand ***********\n'
        hand = self.dealer.deal_hand(2)
        self.player.set_hand(hand)
        self.player.display_hand()
        print '\n'
        print '********* Dealing dealers hand ***********\n'
        dhand = self.dealer.deal_hand(2)
        self.dealer.set_dealer_hand(dhand)
        self.dealer.display_hand(True)
        print '******************************************'
        while not self.game_over:

            self.player.display_hand()
            print '\n'

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
                        self.award_bet('dealer')
                        self.display_balance()
                        self.game_over = True

                elif choice == 2:
                    print 'Let\'s see who won!'
                    if self.check_win(self.player.hand, self.dealer.hand):
                        self.award_bet('player')
                        self.display_balance()
                        print "Blackjack! Congratulations"
                        
                    else:
                        self.award_bet('dealer')
                        self.display_balance()
                        print "The dealer has won"
                    self.dealer.display_hand(False)
                    self.game_over = True

        else:
            print 'The game has ended my dear'
            self.game_loop()

g = Game()