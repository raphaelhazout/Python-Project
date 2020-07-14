a=int(input("select a day: "))
b=int(input("select a month: "))
c=int(input("select a year: "))
if 1<=a<=31 and 1<=b<=12 and 1950<=c<=2020:
    print(a, "/", b, "/", c % 100)
else:
    print("ERROR")



