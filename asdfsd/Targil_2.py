list1=[i for i in range(1,10)]
print(list1)
list2=[]
list2=list1[-3:]
print(list2)
print(list1[::-1])
print(list1[0:14:2])
list3=list1[0:5]
print(list3)
#print(list1[1:14:2])
#a=int(input('choose one number: '))
#list4=list1
#list4[7:9]=[a]
#print(list4)
list4=list1
list5=[]
for i in range(1,10):
    if i%3==0:
        list4.remove(i)
print(list4)
for i in range(1,10):
    if i%3==0:
        list5.append(i)
print(list5)



