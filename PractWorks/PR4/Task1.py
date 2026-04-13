import random

n = int(input("Введите количество чисел: "))

numbers = []

for i in range(0, n):
    randInt = random.randint(1, 100)
    numbers.append(randInt)
    print(f"{i} индекс - {randInt}")
