import random

randInt = random.randint(1, 10)
num = 0

while(num != randInt):
    num = int(input())
    if num > randInt:
        print("Загаданное число меньше")
    elif num < randInt:
        print("Загаданное число больше")
    else:
        print(f"Вы угадали число! {randInt}")

