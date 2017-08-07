from deck import Deck
from dealer import Dealer
from player import Player
from blackjackhand import BlackjackHand

import random
# GameController
class GameController(object):

    def __init__(self):
        self.player_bet = 0

    def prep_player(self):
        self.player = Player(bankroll=100)

    def prep_dealer(self):
        deck = Deck()
        deck.shuffle()
        self.dealer = Dealer(deck)

    def ask_player_bet(self):
        self.player_bet = self.player.ask_bet()

    def hand_to_player(self):
        self.player.take_card(self.dealer.deal_card())
        self.player.take_card(self.dealer.deal_card())
        self.player.show_hand()

    def hand_to_dealer(self):
        self.dealer.take_card(self.dealer.deal_card())
        self.dealer.take_card(self.dealer.deal_card())
        self.dealer.show_hand(True)

    def check_initial_hands(self):
        if self.dealer.hand.is_blackjack() is True and self.player.hand.is_blackjack() is True:
            print("Both you and the Dealer have Blackjack!")
            self.dealer.show_hand()
            return 'tie'

        elif self.dealer.hand.is_blackjack() is True:
            print("Dealer has Blackjack!")
            self.dealer.show_hand(False)
            return 'dealer'

        elif self.player.hand.is_blackjack() is True:
            print("You have Blackjack!")
            return 'player'

        else:
            return 'game goes on'

    def process_blackjack(self, outcome):
        if outcome == 'tie':
            return

        if outcome == 'player':
            self.player.add_win(self.player_bet * 1.5)
            return

        if outcome == 'dealer':
            self.player.sub_loss(self.player_bet)
            return

    def do_player_turn(self):
        while self.player.hand.is_busted() is False:
            decision = self.player.play_turn()
            if decision == "h":
                self.player.take_card(self.dealer.deal_card())
                self.player.show_hand()
            else:
                return

    def check_player(self):
        if self.player.hand.is_busted() is True:
            print("You busted.")
            return 'player_busted'
        else:
            return 'player_ok'

    def do_dealer_turn(self):
        self.dealer.play_turn()

    def check_dealer(self):
        if self.dealer.hand.is_busted() is True:
            print("Dealer busted.")
            return 'dealer_busted'
        else:
            return 'dealer_ok'

    def find_winner(self):
        player_total = self.player.hand.get_total()
        dealer_total = self.dealer.hand.get_total()

        if player_total == dealer_total:
            print("Dealer and Player both have " + str(player_total))
            return 'tie'

        if player_total > dealer_total:
            print("You win with " + str(player_total))
            return 'player'
        else:
            self.dealer.show_hand(False)
            print("Dealer wins with " + str(dealer_total))
            return 'dealer'

    def handle_game_outcome(self, outcome):
        if outcome == 'tie':
            return
        if outcome == 'player':
            self.player.add_win(self.player_bet)
            return
        if outcome == 'dealer':
            self.player.sub_loss(self.player_bet)
            return

    def collect_used_cards(self):
        self.player.empty_hand()
        self.dealer.empty_hand()

    def ask_play(self):
        while True:
            answer = (raw_input('Do you want to play Blackjack? [y/n] ')).lower()
            if answer == 'y':
                return True
            else:
                return False
