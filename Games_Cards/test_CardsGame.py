from unittest import TestCase
from Games_Cards.DecksOfCards import DecksOfCards
from Games_Cards.Card import Card
from Games_Cards.Player import Player
from Games_Cards.CardsGame import CardsGame
from unittest.mock import patch


class test_CardsGame(TestCase):

    def test_constractur(self):
        cards1 = CardsGame(5)
        deck = DecksOfCards()
        cards1.players.append(Player('Raphael', 5000, 5))

        self.assertEqual(cards1.deck, 5)

