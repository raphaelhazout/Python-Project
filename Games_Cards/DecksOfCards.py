from Games_Cards.Card import Card
from random import shuffle

class DecksOfCards:
#הגדרה של חפיסת קלפים
    def __init__(self):
        self.list1=[]
        for suit in ('♠','♥','♦','♣'):
            for value in range(2,15):
                card1=Card(value,suit)
                self.list1.append(card1)
        self.newGame()

    def shuffle(self):
    # עירבוב חפיסת קלפים
        shuffle(self.list1)

    def dealone(self):
    #תחילה בודק אם יש קלפים בחבילה ולאחר מכן מחזיר את הקלף במקום 0 ומוציא אותו מהחפיסה
        if len(self.list1) > 0:
            return self.list1.pop(0)
        return None
    def newGame(self):
    # לוקחת חפיסה חדשה ומערבבת את הקלפים
        self.shuffle()

    def show(self):
    # מציג את החפיסה
        print(self.list1)


