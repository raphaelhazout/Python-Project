def funkk(a,b):
    c=1
    for i in range(b):
        c*=a
    return (c)

a=int(input('choose a number: '))
b=int(input('choose a number: '))
print(funkk(a,b))
