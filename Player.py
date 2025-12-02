from Hand import Hand


class Player(Hand):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.count_of_wins = 0

    def is_want_one_more(self)->bool:
        print(self)
        if not self.is_alive:
            return False
        return input("Do you wanna get one more cards? (Yes/No)") == "Yes"

    def __str__(self):
        result = f"""Player {self.name}, points {self.points}
Hand: {super().__str__()}"""
        return result
