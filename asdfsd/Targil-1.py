def shalosh(a):
    if 99<a<1000:
        return a//100+a//10%10+a%10
a=int(input("choose a number with 3 digits: "))
print(shalosh(a))
