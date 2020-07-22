def aviomo(a):
    b = 0
    for i in range(1,a+1):
        b+=i
    return(b)


a=int(input('choose number: '))

print(aviomo(a))