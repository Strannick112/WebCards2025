from Card import Card


class Hand:
    def __init__(self):
        self.cards = []
        self.points = 0
        self.is_alive = True

    def take(self, card: Card):
        if self.is_alive:
            self.cards.append(card)
            self.points += card.rang.points
            if self.points > 21:
                self.points = 0
                self.is_alive = False

    def drop_cards(self):
        self.cards = []
        self.points = 0
        self.is_alive = True

    def __str__(self):
        result = ""
        for card in self.cards:
            result += card.__str__() + ", "
        result = result[:-2]
        return result

