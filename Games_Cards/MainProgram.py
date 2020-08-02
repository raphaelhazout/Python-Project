from Games_Cards.Player import Player
from Games_Cards.DecksOfCards import DecksOfCards
from Games_Cards.Card import Card
from Games_Cards.CardsGame import CardsGame
game1 = CardsGame(5)
print(game1)
bet=0
list1=[]
winner1=0
winner2=0

for i in range(5):
    bet = bet + 100
    for y in game1.players:
        y.reduceAmount(bet)
        list1.append(y.getCard())
    if list1[0]>list1[1]:
        winner1=0
    else:
        winner1=1
    if list1[2]>list1[3]:
        winner2=2
    else:
        winner2=3
    if list1[winner1]>list1[winner2]:
        pass
    else:
        winner1=winner2
    prize = bet * 4
    Winner=game1.players[winner1]
    Winner.addAmount(prize)
    print(list1)
    print(Winner)
    list1.clear()



