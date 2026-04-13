s = input("Строка: ")
repS = ""

for i in range(0,len(s)):
    if i == 0 or i == len(s) - 1:
        repS = repS + '#'
    else:
        repS = repS + s[i]
print(repS)