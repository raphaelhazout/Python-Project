from unittest import TestCase
from Games_Cards.DecksOfCards import DecksOfCards
from Games_Cards.Card import Card
from Games_Cards.Player import Player
from Games_Cards.CardsGame import CardsGame
from unittest.mock import patch
class Test_Player(TestCase):
    # בודק אם חילקתי 5 קלפים אז אורך היד היא באמת 5
    def test_set_hand(self):
        player1=Player('avi',1200,5)
        deck1=DecksOfCards()
        player1.setHand(deck1)
        self.assertEqual(len(player1.hand) , 5)

    def test_set_hand2(self):
    # בדיקה בסיסית שהסט עובד
        with patch('Games_Cards.DecksOfCards.DecksOfCards.dealone') as mockdeal1:
            card2=Card(8,'♥')
            mockdeal1.return_value=card2
            deck1=DecksOfCards()
            Raphael=Player('Raphael',5000)
            Raphael.setHand(deck1)
            self.assertEqual(Raphael.hand[0],card2)

    def test_get_card(self):
    # בודק מה קורה כשאין לשחקן קלפים
       player1=Player('Raphael',5000)
       player1.getCard()
       self.assertTrue(len(player1.hand) == 0)

    def test_get_card2(self):
    # בודק אם כשאני מושך קלף מהשחקן אז יורד לו הכמות באחד
        player1 = Player('Raphael', 5000,5)
        deck=DecksOfCards()
        player1.setHand(deck)
        player1.getCard()
        self.assertTrue(len(player1.hand) -1)


    def test_add_card(self):
    # בודק אם כשאני מוסיף לו קלף אז הכמות עולה באחד
        player1=Player('Raphael', 5000,5)
        deck = DecksOfCards()
        player1.setHand(deck)
        len1=len(player1.hand)
        player1.addCard(deck)
        self.assertEqual(len(player1.hand), 6)

    def test_add_card2(self):
    # המוק מחזיר לי ערך של קלף וכשאני מוסיף קלף אז הוא
        with patch('Games_Cards.DecksOfCards.DecksOfCards.dealone') as mockdeal1:
            card2=Card(8,'♥')
            mockdeal1.return_value=card2
            deck1=DecksOfCards()
            Raphael=Player('Raphael',5000)
            Raphael.addCard(deck1)
            self.assertEqual(Raphael.hand[0],card2)



    def test_reduce_amount(self):
    # בודק כשאני מוריד את הכמות כסף באלף היא אכן יורדת
        player1=Player('Raphael', 5000,5)
        deck = DecksOfCards()
        player1.reduceAmount(1000)
        self.assertTrue(player1.money == 4000)

    def test_reduce_amount2(self):
        #בדיקה אם הAMOUNT קטן מתחת לאפס אז לא ירד כסף
        player1 = Player('Raphael', 5000, 5)
        deck = DecksOfCards()
        player1.reduceAmount(-1000)
        self.assertTrue(player1.money == 5000)
    def test_reduce_amount3(self):
        #בדיקה אם הAMOUNT קטן מתחת לאפס אז לא ירד כסף
        player1 = Player('Raphael', 5000, 5)
        deck = DecksOfCards()
        player1.reduceAmount(0)
        self.assertTrue(player1.money == 5000)

    def test_add_amount(self):
        # בודק כשאני מוסיף את הכמות כסף באלף היא אכן יורדת
        player1 = Player('Raphael', 5000, 5)
        deck = DecksOfCards()
        player1.addAmount(1000)
        self.assertEqual(player1.money , 6000)

    def test_add_amount2(self):
    # בודק אם אני לא מוסיף כסף אז הערך של הכסף נשאר אותו דבר
        player1 = Player('Raphael', 5000, 5)
        deck = DecksOfCards()
        player1.addAmount(0)
        self.assertEqual(player1.money, 5000)


    def test_add_amount3(self):
    #בודק אם אני מוסיף מינוס אז לא יורד כלום
        player1 = Player('Raphael', 5000, 5)
        deck = DecksOfCards()
        player1.addAmount(-10)
        self.assertEqual(player1.money, 5000)

