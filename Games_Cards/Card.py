
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

