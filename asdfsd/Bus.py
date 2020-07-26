class Buss:
    def __init__(self,moshavim,):
        self.list1 = []
        self.moshavim=moshavim
        for i in range(self.moshavim):
            self.list1.append('free')
    def getOn(self,passenger):
        for i in range(len(self.list1)):
            if self.list1[i]=='free':
                self.list1[i]=passenger
                break
        else:
            print('The buss is full.The passenger: ',{passenger},'is not on the buss')
    def getOff(self,passenger):
        for i in range(len(self.list1)):
            if self.list1[i]==passenger:
                self.list1[i]='free'
                break
        else:
            print('The passenger: ',{passenger},'is not on the buss.')
    def __str__(self):
        return f'the list of the passenger is {self.list1}, and the number of moshavim is: {self.moshavim}'


buss1=Buss(10)
a=int(input('choose a number from 0-2'))
while a!=0:
    if a==1:
        buss1.getOn(input('choose name: '))
    if a==2:
        buss1.getOff(input('choose name: '))
    a = int(input('choose a number from 0-2'))
    print(buss1)


#s