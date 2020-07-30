count=0
max=0
sum=0
a = int(input("Put your Number: "))
while a>=0 and a<101:
    count+=1
    sum+=a
    if a>max:
        max=a
    a = int(input("Put your Number: "))
average=sum/count
print(average)
print(max)
print(max-average)
