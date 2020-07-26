from random import randint
class Lottery:
    def lott(self):
        self.list1=[]
        for i in range(6):
            self.list1.randint(1,45)
    def max(self):
        b=int(input('Whats The Maximum win? '))

    def __init__(self):
        self.lott()
        self.max()

    def misparim(self):
        print(self.list1)

    def nihush(self,number):
        for i in self.list1(1,45):
            if i==number:
                return True
        return False

    def nihushim(self,number,win):
        for i in self.list1(1,45):
            a=0
            if i==number:
                a+=1
        if a<=1:
            win=0
        if 2<a<5:
            win=a*b/6
        if a==6:
            win=b

lott1=Lottery()
for i in range(6):
    num=int(input('choose number bitween 1-45: '))
    if 1<num<45:
        lott1.nihush(num)
    else:
        print('invalid number')

