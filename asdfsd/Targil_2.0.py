def shalosh(a):
    if a in range(100,1000):
        return True
    else:
        return False
a=int(input('choose a number: '))
if shalosh(a):
    print('Ben shalosh sfarot')
else:
    print('cos emek')
