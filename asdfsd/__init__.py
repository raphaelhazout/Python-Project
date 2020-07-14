a=int(input("what is your age?  "))
if 0<=a<=18:
    print("child")
elif 19<=a<=60:
    print("adult")
elif 61<=a<=120:
    print("senior")
else:
    print("ERROR")
