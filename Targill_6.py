def hanaha(a,b):
    if a<10:
        return 100
    if 10<a<18 and b!='Jerusalem':
        return 25
    if 10<a<18 and b=='Jerusalem':
        return 35
    if 18<a<60 and b=='Jerusalem':
        return 10
    if a>60:
        return 50
    return 0
def hanaha2(d,b):
    return d-(d*b/100)

a=int(input('whats your age? '))
b=input('where are you live? ')
d=int(input('whats the price? '))
print(hanaha2(d,hanaha(a,b)))