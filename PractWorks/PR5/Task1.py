s = input("Введите строку: ")

print(s * 5)

print(f"Длина строки: {len(s)}")

for i in range(0, len(s)):
    print(f"{i} - {s[i]}")

print()

for i in range(0, len(s)):
    if i % 2 == 0:
        print(f"{i + 1} - {s[i]}")