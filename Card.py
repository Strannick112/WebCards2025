from Mast import Mast, masts
from Rang import Rang


class Card:
    def __init__(self, rang: str, mast: Mast):
        self.rang = Rang(rang)
        self.mast = mast

    def __str__(self):
        return f"{self.rang}{self.mast}"

# Небольшой тест
# card = Card(rang=Rang("6"), mast=Mast(masts[0]))
# print(card)
