try:
    a = int(input("1: "))
    flag = True
    while flag == True:
        b = int(input("2: "))
        try:
            result = a/b
            flag = False
        except ZeroDivisionError:
            print(f"Невозможно поделить {a} на {b}")
finally:
    print(f"{a} / {b} = {result}")