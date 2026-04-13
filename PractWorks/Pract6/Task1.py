try:
    a = int(input("1: "))
    b = int(input("2: "))
    print(f"{a} / {b} = {a/b}")
except ZeroDivisionError:
    print(f"Невозможно поделить {a} на {b}")