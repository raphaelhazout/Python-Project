def numb(a):
    b=0
    for i in range(1,a+1):
        b+=i
        print(b)
if __name__=='__main__':
    a=int(input('choose a number: '))
    numb(a)

