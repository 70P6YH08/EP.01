s1 = input("Строка 1: ")
s2 = input("Строка 2: ")

lenS2 = len(s2)
lenS1 = len(s1)

count = 0

for i in range(0, lenS2):
    if s2.find(s1, i, i + lenS1) != -1:
        print(s2.find(s1, i, i + lenS1))
        count+=1
print()
print(f"Количество вхождений s1 в s2 = {count}")