s = input("Строка: ")

while "  " in s:
    s = s.replace("  "," ")
print(s)