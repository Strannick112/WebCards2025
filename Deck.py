import random
from Card import Card
from Mast import masts
from Rang import rangs


class Deck:
    def __init__(self):
        self.__deck = []
        for rang in rangs.keys():
            for mast in masts:
                self.__deck.append(Card(rang, mast))
        self.__current_card = None
        self.sort()

    def sort(self):
        random.shuffle(self.__deck)
        self.__current_card = self.__deck.__iter__()

    def get(self)-> Card:
        return self.__current_card.__next__()

# Небольшой тест
# deck = Deck()
# for i in range(36):
#     print(deck.get())
