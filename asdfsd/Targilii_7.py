from random import randint
list1=[]
def funk(a,b,c):
    for i in range(c):
        list1.append(randint(a,b))


a=int(input('lower: '))
b=int(input('upper: '))
c=int(input('sum of numbers: '))
funk(a,b,c)