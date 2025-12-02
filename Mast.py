class Mast:
    def __init__(self, title):
        self.title = title
        if self.title not in masts:
            raise NameError("Mast doesn't exist")

    def __str__(self):
        return self.title

masts = ("♦", "♥", "♠", "♣")
