from cmath import sqrt

try:
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    result = sqrt(x + y + z)/(x-y+z) ** 2

    underSqrt = x + y + z

    if underSqrt < 0:
        raise ValueError("Под корнем < 0!!!")
    print(result)
except ValueError as msg:
    print(f"Ошибка: {msg}")
except ZeroDivisionError:
    print("На 0 делить нельзя")