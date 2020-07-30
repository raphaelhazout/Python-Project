from Games_Cards.Player import Player
from Games_Cards.DecksOfCards import DecksOfCards
from Games_Cards.Card import Card
from Games_Cards.CardsGame import CardsGame
game1 = CardsGame(5)
print(game1)
bet=0
list1=[]
for i in range(5):
    bet = bet + 100
    for y in game1.players:
        y.reduceAmount(bet)
        list1.append(y.getCard())




prize = bet*4


