import random

randInt = random.randint(1, 1000)
isSimple = False

for i in range(1, randInt - 1):
    if randInt % i == 0 and i != 1:
        isSimple = True
        break

if isSimple == True:
    print(f"{randInt} - не простое")
else:
    print(f"{randInt} - простое")