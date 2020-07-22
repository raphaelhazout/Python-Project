from random import randint
l=0
h=100
count=0
r=randint(l,h)
print(r)
an=input('is the guess correct? ')
while an!='correct':
    if an=='low':
        l=r+1
    else:
        h=r-1
    r=randint(l,h)
    print(r)
    count += 1
    an=input('is the guess correct? ')
print('Succes')
print(count)


