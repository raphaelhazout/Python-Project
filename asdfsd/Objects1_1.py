
class Person:
    def __init__(self, name, age, numchild):
        self.name=name
        self.age=age
        self.numchild=numchild

    def haschild(self):
        if self.numchild>0:
            return True
        else:
            return False

    def agegroup(self):
        if 0<self.age<18:
            return 'Child'
        elif 19<self.age<60:
            return 'Adult'
        elif 61<self.age<120:
            return 'Senior'


    def __str__(self):
        return (f'My name is {self.name}, my age is {self.age}, i have {self.numchild} kids.')
person1=Person('Raphael',21,1)
print(person1)
print(person1.haschild())
print(person1.agegroup())