from unittest import TestCase
from Games_Cards.DecksOfCards import DecksOfCards
from Games_Cards.Card import Card
from Games_Cards.Player import Player
from Games_Cards.CardsGame import CardsGame
from unittest.mock import patch


class test_CardsGame(TestCase):

    def test_Constructor(self):
        with patch('Games_Cards.CardsGame.CardsGame.newGame') as mockdeal1:
            game1=CardsGame(0)
            self.assertEqual(game1.numcards,5)
