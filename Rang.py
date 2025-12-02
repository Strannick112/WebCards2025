class Rang:
    def __init__(self, title):
        self.title = title
        if self.title in rangs.keys():
            self.points = rangs[self.title]
        else:
            raise NameError("Rang doesn't exist")

    def __str__(self):
        return self.title


rangs = {
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "X": 10,
    "J": 2,
    "Q": 3,
    "K": 4,
    "A": 11
}
