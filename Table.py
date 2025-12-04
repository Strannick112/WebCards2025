from Deck import Deck
from Player import Player


class Table:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.__players_iterator = None
        self.current_player = None

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def prepare(self):
        self.__players_iterator = self.players.__iter__()
        self.current_player = self.__players_iterator.__next__()
        for player in self.players:
            player.take(self.deck.get())

    def start(self):
        for player in self.players:
            # print(player)
            while player.is_want_one_more():
                player.take(self.deck.get())

    def give_card_to_player(self):
        if self.current_player.is_alive:
            self.current_player.take(self.deck.get())
        else:
            self.current_player = self.__players_iterator.__next__()

    def turn_move(self):
        self.current_player = self.__players_iterator.__next__()

    def get_winners(self):
        max_points = 0
        for player in self.players:
            if player.points > max_points:
                max_points = player.points

        winners = []
        for player in self.players:
            if player.points == max_points:
                winners.append(player)

        return winners

    def print_winners(self):
        winners = self.get_winners()
        count_of_winners = len(winners)
        if count_of_winners == 0:
            print("You are everyone greedy loosers >:<")
        elif count_of_winners == 1:
            print(f"{winners[0].name} is winner!")
        else:
            print(f"There is {count_of_winners} winners!")
            for winner in winners:
                print(f"{winner.name} is winner!")
