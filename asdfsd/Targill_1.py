def ful(b):
    str1=""
    for i in b:
        if i!='a':
            str1+=i
    return str1

b=input('write something: ')
print(ful(b))
