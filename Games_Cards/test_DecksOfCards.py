from unittest import TestCase
from Games_Cards.DecksOfCards import DecksOfCards
from Games_Cards.Card import Card
from Games_Cards.Player import Player
from Games_Cards.CardsGame import CardsGame
class test_DeckOfCards(TestCase):

    def test_shuffle(self):
    # בדיקת לפונקצייה האם היא אכן מערבבת את החבילה
        deck1=DecksOfCards()
        deck2=deck1
        deck1.shuffle()
        if self.assertTrue(deck1 == deck2):
            print(True)
        else:
            print(False)
    def test_shuffle2(self):
    # בדיקה לפונקציה אחרי שאני מוציא קלף מראש החפיסה אני מערבב אותה ומשווה לחפיסה לפני העירבוב
        deck1=DecksOfCards()
        deck1.dealone()
        deck2=deck1
        deck1.shuffle()
        if self.assertTrue(deck1 == deck2):
            print(True)
        else:
            print(False)

    def test_dealone(self):
    #בודק אם אורך של חפיסה אחרי חילוק קלף יורד ל51
        deck1=DecksOfCards()
        deck1.dealone()
        self.assertTrue(len(deck1.list1)==51)
    def test_dealone2(self):
    #בדיקה אם כאשר אני מחלק את כל החפיסה אז אורך החפיסה שווה לאפס
        deck1= DecksOfCards()
        for i in range(52):
            deck1.dealone()
        self.assertTrue(len(deck1.list1) == 0)
        self.assertEqual(deck1.dealone(), None)

    def test_new_game(self):
        deck1=DecksOfCards()
        deck2=DecksOfCards()
        self.assertTrue(deck1.newGame() != deck2)

    def test_new_game2(self):
        deck1=DecksOfCards()
        deck2=deck1
        deck1.list1[0] != deck2.list1[0]



    def test_show(self):
         pass
