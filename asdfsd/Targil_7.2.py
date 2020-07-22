dic1={1:32,2:35,3:923,4:78}
dic2={}
#print(dic1.items())
for i in dic1.items():
    dic2[i[1]]=i[0]
print(dic2)
