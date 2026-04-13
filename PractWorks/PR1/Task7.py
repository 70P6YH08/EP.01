a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

temp = b
b = a
a = temp
print(f"Первое число: {a}")
print(f"Второе число: {b}")