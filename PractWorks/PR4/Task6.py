
n = int(input("Введите количество элементов для добавления: "))
numbers1 = [4,5,2,3,4,5,2,23]

for i in range(0, n):
    index = int(input("Индекс элемента для вставки: "))
    item = int(input("Значение элемента для вставки: "))
    print()
    numbers1.insert(index, item)
print(numbers1)