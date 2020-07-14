a = int(input("choose a number: "))
min = 0
while a > 0 or a < 0:
    if a > 0:
        if a < min or min == 0:
            min = a
    a = int(input("choose a number: "))
print(min)
