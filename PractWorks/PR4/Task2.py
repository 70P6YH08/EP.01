import random

n = int(input("Введите количество чисел: "))

numbers = []

for i in range(0, n):
    num = int(input(f"Введите {i + 1} элемент списка: "))
    numbers.append(num)
print(numbers)
