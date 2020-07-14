a = int(input("Choose one number:  "))
b = int(input("Choose one number:  "))
while a % 2 == 0 and b % 2 == 0:
    print(a + b)
    a = int(input("Choose one number:  "))
    b = int(input("Choose one number:  "))
print(a * b)
