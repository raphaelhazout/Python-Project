
class Card:
#חפיסת קלפים- כל קלף בעל ערך של מספר ושל סמל
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit

    def __repr__(self):
        #מחזיר את פרטי האובייקט, ומוגדר לו שכל מספר מעל עשר מה הערך שלו
        if self.value == 11:
            return (f'J{self.suit}')
        if self.value == 12:
            return (f'Q{self.suit}')
        if self.value == 13:
            return (f'K{self.suit}')
        if self.value == 14:
            return (f'A{self.suit}')
        return (f'{self.value}{self.suit}')
    def __gt__(self, other):
    # הגדרה של הערכים של הצורות
        values=[]
        suits=['♦','♠','♥','♣']
        for value in range(2, 15):
            values.append(value)
        if(self.value>other.value):
            return True
        elif(self.value<other.value):
            return False
        else:
            mys=0
            others=0
            for suit in range (0,4):
                if(suits[suit]==self.suit):
                    mys=suit
                if(suits[suit]==other.suit):
                    others=suit
            if(mys>others):
                return True
            else:
                return False



