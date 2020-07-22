def age():
    for i in range(5):
        a = int(input(('what is your age? ')))
        if 0<a<18:
            print('child')
        if 19<a<60:
            print('adult')
        if 61<a<120:
            print('senior')
age()

