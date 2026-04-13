a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))

if a > b:
    if b > c:
        print(b)
    elif b < c:
        if a < c:
            print(a)
        else:
            print(c)
elif a < b:
    if b < c:
        print(b)
    elif b > c:
        if a > c:
            print(a)
        else:
            print(c)