a=int(input("what is the present of the factor? "))
sum=0
bum=0
for i in range(5):
    b=int(input("what is the grade? "))
    c=b+(b*20/100)
    print(c)
    sum+=c
    bum+=b
print(sum/5)
print(bum/5)
print(sum/5-bum/5)