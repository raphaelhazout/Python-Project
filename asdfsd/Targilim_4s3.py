count=0
max=0
countmax=0
for i in range(7):
    a = int(input("Choose a number :)  : "))
    count+=1
    if a>max:
        max=a
        countmax=count
print(max)
print(countmax)