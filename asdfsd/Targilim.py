def rand_k_num(a):
    b=a%10+a//10%10+a//100

    return b

a=int(input('choose a number: '))
print(rand_k_num(a))