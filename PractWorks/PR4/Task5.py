import random

num = int(input("Введите число: "))
numbers1 = [0,1,1,2,34,5,2,1,2,3,2,3,25,61,7,84,7,3,63,31,2,342]
print(numbers1.count(num))

numbers2 = []
for i in range(0, len(numbers1) - 1):
    if numbers1[i] != num:
        numbers2.append(numbers1[i])
print(numbers2)