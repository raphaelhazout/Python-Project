list1=[i for i in range(1,11)]
print(list1)
list2=[]
list2=list1[-3:]
print(list2)
print(list1[::-1])
print(list1[1:14:2])
list3=list1[0:14:2]
print(list3)
list4=(input('choose 3 number: ')).split()
print(list4)
list1[4:5]=list4[0]+list4[1]
print(list1)

