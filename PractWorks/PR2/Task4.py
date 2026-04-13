from math import pow

a = int(input("1 сторона: "))
b = int(input("2 сторона: "))
c = int(input("3 сторона: "))

if a + b > c and b + c > a and a + c > b:
    print("Такой треугольник существует.")
    if a == b or b == c or c == a:
        print("Он равнобедренный")
    elif a == b == c:
        print("Он равносторонный")
    elif pow(a,2) + pow(b,2) == pow(c,2) or pow(b,2) + pow(c,2) == pow(a,2) or pow(a,2) + pow(c,2) == pow(b,2):
        print("Он прямоугольный")
else:
    print("Такого треугольника не существует")