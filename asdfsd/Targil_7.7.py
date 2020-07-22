dic1={1:10,2:20,3:10,4:30}
dic2={}
dic3={}
for i in dic1.items():
    dic2[i[1]]=i[0]

dic1.clear()
for i in dic2.items():
    dic1[i[1]]=i[0]
print(dic1)

