dic1={1:20,2:30,30:2}
a=int(input('choose a key: '))
if a in dic1:
    del dic1[a]
print(dic1)