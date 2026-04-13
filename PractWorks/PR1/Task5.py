num = float(input("Введите вещественное число: "))
n = int(input("Количество знаков после запятой: "))

print("{:.3f}".format(num))
print(round(num,n))