from blackjackhand import BlackjackHand

# Player
class Player(object):

    def __init__(self, bankroll = 100):
        self.bankroll = bankroll
        self.hand = BlackjackHand()

    def add_win(self, amount):
        self.bankroll += amount
        print("You win $" + str(amount) +". You now have $" + str(self.bankroll) + " in hand." )

    def sub_loss(self, amount):
        self.bankroll -= amount
        print("You lose $" + str(amount) +". You have $" + str(self.bankroll) + " left." )
        if amount < 0:
            print "WARNING: you owe $", -amount, "this should not happen! (exception)"

    def take_card(self, card):
        self.hand.add_card(card)

    def empty_hand(self):
        self.hand = BlackjackHand();

    def show_hand(self):
        print("Your hand:")
        self.hand.show()

    def ask_bet(self):
        bet = 0
        while True:
            try:
                bet = int(raw_input("\nWhat is your bet? "))
            except:
                continue
            finally:
                if bet == self.bankroll:
                    print "Betting the farm!"

                if bet > 0 and self.bankroll - bet >= 0:
                    print('-------------------------------------------')
                    return bet

                if bet < 0:
                    print "Bet must be a positive amount"

                if self.bankroll - bet < 0:
                    print "You don't have enough money for this bet"

    def play_turn(self):
        while True:
            turn = (raw_input("Do you wish to [h]it or [s]tay? ")).lower()
            if turn not in "hs":
                continue
            else:
                return turn
