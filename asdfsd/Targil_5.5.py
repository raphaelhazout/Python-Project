list1=input('give your fucking grades: ').split()
a=0
b=0
for i in list1:
    if (0<int(i)<60):
        a+=1
    elif (100>int(i)>60):
        b+=1
print(a,b)
