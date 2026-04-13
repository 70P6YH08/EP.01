from math import pi, pow, e, sin, sqrt

x = int(input("Введите x:"))

if x < -10:
    print(pi * pow(x,2))
elif x >= -10 & x < -5:
    print(pow(x,4))
elif x >= -5 & x < 10:
    print(e*abs(x))
else:
    print(1/sin(sqrt(x)))