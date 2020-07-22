num1=int(input('put 1'))
num2=int(input('put2'))
if num1>num2:
    num1, num2 = num2, num1
for i in range(num1,num2):
    if i%2==0  :
        print(i)




