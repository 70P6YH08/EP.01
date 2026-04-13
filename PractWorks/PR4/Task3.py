import random

numbers1 = [0,1,2,3,4,5]
numbers2 = [6,7,8,9,10,121,12,123,12,4,13,7,1,82]

for i in range(0, len(numbers2)):
    if numbers2[i] % 2 == 0:
        numbers1.append(numbers2[i])
for i in range(0, len(numbers1)):
    print(numbers1[i], end = " ")
