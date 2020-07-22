from random import randint
R=randint(1,9)
a=int(input('guess the number: '))
while a!=R:
    if a>R:
        print('LOWER')
    else:
        print('HIGHER')
    a = int(input('guess the number: '))
print('Great')