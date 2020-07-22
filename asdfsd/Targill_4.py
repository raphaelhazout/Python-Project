def rishoni(a):
    for i in range(2,a):
        if a%i==0:
            return False
            break
    else:
        return True

a=int(input('choose number'))
if rishoni(a):
    print('rishoni')
else:
    print('lo rishoni')
