# BlackjackHand
class BlackjackHand(object):

    values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_total(self):
        sum = 0
        for card in self.cards:
            sum += BlackjackHand.values[card.rank]

        for card in self.cards:
            if card.is_ace() and sum <= 11:
                sum += 10

        return sum

    def is_blackjack(self):
        total = self.get_total()
        return total == 21 and len(self.cards) == 2

    def is_busted(self):
        return self.get_total() > 21

    def is_dealer_limit(self):
        return self.get_total() >= 17

    def show(self, hide_card=False):
        if hide_card is True and len(self.cards) > 0:
            print("#:#")
            for card in self.cards[1:]:
                print(card)
        else:
            for card in self.cards:
                print(card)
        print('-------------------------------------------')
