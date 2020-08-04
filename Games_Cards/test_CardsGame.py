from unittest import TestCase
from Games_Cards.DecksOfCards import DecksOfCards
from Games_Cards.Card import Card
from Games_Cards.Player import Player
from Games_Cards.CardsGame import CardsGame
from unittest.mock import patch


class test_CardsGame(TestCase):

    def test_Constructor(self):
     #בודק אם מחלקים אפס קלפים אז שהשחקן מקבל 5 קלפים כברירת מחדל
        with patch('Games_Cards.CardsGame.CardsGame.newGame') as mockdeal1:
            game1=CardsGame('d' 'e' 'r' 't',0)
            self.assertEqual(game1.numcards,5)

    def test_Constructor2(self):
    # בודק אם מזינים סטרינג במספר חילוק קלפים אז הוא מחלק 5 כברירת מחדל
        with patch('Games_Cards.CardsGame.CardsGame.newGame') as mockdeal1:
            game1=CardsGame('d' 'e' 'r' 't','sve')
            self.assertEqual(game1.numcards,5)

    def test_Constructor3(self):
    # בודק אם מחלקים מספר גבוהה של קלפים אז הוא נותן 13 כמספר מקסימלי לחילוק
        with patch('Games_Cards.CardsGame.CardsGame.newGame') as mockdeal1:
            game1=CardsGame('d' 'e' 'r' 't',255)
            self.assertEqual(game1.numcards,13)

    def test_Constructor4(self):
        with patch('Games_Cards.CardsGame.CardsGame.newGame') as mockdeal1:
            game1=CardsGame('d' 'e' 'r' 't',7)
            self.assertEqual(game1.numcards,7)