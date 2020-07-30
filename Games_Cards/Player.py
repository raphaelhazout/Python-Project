from Games_Cards.Card import Card
from Games_Cards.DecksOfCards import DecksOfCards
from random import shuffle

class Player:

    def __init__(self,name,money,cards=5):
    #הגדרה של שחקן:שם,כמות כסף,קלפים
        self.name=name
        self.money=money
        self.cards=cards
        self.hand=[]


    def setHand(self,deck,cards=5):
    #נותנת לשחקן חבילת קלפים- ברירת מחדל 5 קלפים
        if cards <=0:
            self.cards=5
        for i in range(self.cards):
            self.hand.append(deck.dealone())

    def getCard(self):
    #תחילה בודק אם יש לשחקן קלפים בכלל, מערבב את החבילה ואז לוקח את הקלף הראשון
        if len(self.hand) > 0:
            shuffle(self.hand)
            self.hands.pop(0)
        else:
            print('The Player dont have Cards!!!')

    def addCard(self,Deck):
    # מוסיפה קלף לשחקן
        self.hand.append(Deck.dealone())

    def reduceAmount(self,amount):
    # מורידה כמות כסף שהוזן מקופת השחקן
        self.money-=amount

    def addAmount(self,amount):
    # מוסיפה כמות כסף שהוזן מקופת השחקן
        self.money+=amount

    def __repr__(self):
    # מדפיסה את פרטי השחקן
        return f'The player {self.name}, the amount of money that he have:{self.money}, and the cards he have: {self.hand}\n'





#d3=Player('ben',300,5)
#d = DecksOfCards()
#d3.setHand(d)
