
class Animel:
    def __init__(self,name,hunger=5,energy=5):
        self.name=name
        self.hunger=hunger
        self.energy=energy

    def __str__(self):
        return f'The name of the Animal is: {self.name}\nthe hunger of the animal: {self.hunger}\nthe energy of the animal is {self.energy}'

    def eat(self, amount):
        self.hunger-=amount/50
        if self.hunger<0:
            self.hunger=0
            print('the Animal eat to much')
        self.energy-=amount/100
        if self.energy<0:
            self.energy=0

    def play(self,time):
        self.energy-=time/5
        self.hunger+=time/5
        if self.energy<0:
            self.energy=0
            print('Game over, The Animal is tired.')
        if self.hunger>10:
            self.hunger=10

    def rest(self,rtime):
        self.energy+=rtime/20
        self.hunger+=rtime/30
        if self.energy>10:
            self.energy=10
            print('im finish to rest')
            self.hunger=rtime/30
        if self.hunger>10:
            self.hunger=10
            print('i finish to rest i want to eat!')
            self.energy+=rtime/20

animel1=Animel('avi',5,5)
animel1.rest(200)
print(animel1)
a=int(input('choose number: '))
