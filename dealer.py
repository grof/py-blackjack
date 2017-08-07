from blackjackhand import BlackjackHand

# Dealer
class Dealer(object):

    def __init__(self, deck):
        self.deck = deck
        self.hand = BlackjackHand()

    def deal_card(self):
        # we assume we will not run out of cards
        # given we only have 2 players and they won't
        # get through all the cards. Deck is recreated
        # each game
        return self.deck.draw()

    def take_card(self, card):
        self.hand.add_card(card)

    def empty_hand(self):
        self.hand = BlackjackHand()

    def play_turn(self):
        while True:
            if self.hand.is_dealer_limit() is True or self.hand.is_busted() is True:
                break;

            print "Dealer draws card"
            self.hand.add_card(self.deck.draw())
            self.show_hand()
            continue

    def show_hand(self, hide_card = True):
        print("Dealer's hand:")
        self.hand.show(hide_card)
