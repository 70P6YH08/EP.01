n = int(input("n: "))
a = float(input("a: "))
b = float(input("b: "))
x1 = float(input("x1: "))
x2 = float(input("x2: "))

step = abs(x2-x1) / n

if x1 < x2:
    while x1 < x2:
        print(f"y({round(x1,3)}) = {round(a*x1+b, 3)}")
        x1 += step

elif x1 > x2:
    while x1 > x2:
        print(f"y({round(x2,3)}) = {round(a*x2+b, 3)}")
        x2 += step
else:
    print(f"y({round(x1,3)}) = {round(a*x1+b, 3)}")