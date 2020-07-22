l=[]
num=0
while (num==0):
    a=input("הכנס ערך,עד שאתה מקבל f")
    if(a=='f'):
        num=1
    else:
        l.append(a)

l1=[]
num1=0
while (num1==0):
    a2=input("הכנס ערך לרשימה השנייה,עד שאתה מקבל f")
    if(a2=='f'):
        num1=1
    else:
        l1.append(a2)
print(l1+l)
print(len(l+l1))







